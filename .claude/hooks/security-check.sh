#!/bin/bash
# Security validation hook for PreToolUse
# Prevents dangerous operations and checks for security issues

set -e

# Read JSON input
json_input=$(cat)

# Extract tool information
tool_name=$(echo "$json_input" | jq -r '.tool_name // empty')
command=$(echo "$json_input" | jq -r '.tool_args.command // empty')
file_path=$(echo "$json_input" | jq -r '.tool_args.file_path // empty')

# Check for dangerous bash commands
if [[ "$tool_name" == "Bash" ]]; then
    # Dangerous patterns
    dangerous_patterns=(
        "rm -rf /"
        "rm -rf *"
        "chmod 777"
        "curl.*\|.*sh"
        "wget.*\|.*sh"
        "> /dev/sda"
        "dd if=/dev/zero"
        ":(){ :|:& };:"
    )

    for pattern in "${dangerous_patterns[@]}"; do
        if echo "$command" | grep -qE "$pattern"; then
            echo "🚨 BLOCKED: Dangerous command pattern detected: $pattern"
            echo "If this is intentional, please run the command manually."
            exit 2  # Exit code 2 blocks the operation
        fi
    done

    # Warn about sudo usage
    if echo "$command" | grep -q "sudo"; then
        echo "⚠️  Warning: sudo command detected. Please ensure this is necessary."
    fi
fi

# Check for secrets in files
if [[ "$tool_name" =~ ^(Write|Edit|MultiEdit)$ ]] && [[ -n "$file_path" ]]; then
    # Get file content from tool_args
    content=$(echo "$json_input" | jq -r '.tool_args.content // .tool_args.new_string // empty')

    # Check for potential secrets
    secret_patterns=(
        "AKIA[0-9A-Z]{16}"  # AWS Access Key
        "-----BEGIN.*PRIVATE KEY-----"  # Private Key
        "ghp_[a-zA-Z0-9]{36}"  # GitHub Personal Access Token
        "gho_[a-zA-Z0-9]{36}"  # GitHub OAuth Token
        "sk-[a-zA-Z0-9]{48}"  # OpenAI API Key
    )

    for pattern in "${secret_patterns[@]}"; do
        if echo "$content" | grep -qE "$pattern"; then
            echo "🔐 WARNING: Potential secret detected matching pattern: $pattern"
            echo "Please use environment variables instead of hardcoding secrets."
            echo "Add to .env file and reference with os.getenv() or process.env"
            # Don't block, just warn
        fi
    done
fi

# Check for unsafe Django settings
if [[ "$file_path" =~ settings.*\.py$ ]]; then
    content=$(echo "$json_input" | jq -r '.tool_args.content // .tool_args.new_string // empty')

    if echo "$content" | grep -q "DEBUG.*=.*True" && [[ "$file_path" =~ production ]]; then
        echo "❌ BLOCKED: DEBUG=True detected in production settings!"
        exit 2
    fi

    if echo "$content" | grep -q "SECRET_KEY.*=.*['\"]"; then
        echo "⚠️  Warning: Hardcoded SECRET_KEY detected. Use environment variables."
    fi
fi

exit 0

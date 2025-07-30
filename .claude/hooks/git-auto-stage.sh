#!/bin/bash
# Automatically stage files to git after modifications
# Use with PostToolUse hook

set -e

# Read JSON input
json_input=$(cat)

# Extract file path
file_path=$(echo "$json_input" | jq -r '.tool_args.file_path // empty')
tool_name=$(echo "$json_input" | jq -r '.tool_name // empty')

# Only process file modification tools
if [[ ! "$tool_name" =~ ^(Write|Edit|MultiEdit)$ ]] || [[ -z "$file_path" ]]; then
    exit 0
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir &> /dev/null; then
    exit 0
fi

# Check if file exists and is not in .gitignore
if [[ -f "$file_path" ]] && ! git check-ignore "$file_path" &> /dev/null; then
    # Stage the file
    git add "$file_path"
    echo "📝 Auto-staged: $file_path"

    # Show brief status
    changes=$(git diff --cached --name-status | wc -l)
    echo "📊 Total staged changes: $changes files"
fi

#!/bin/bash
# Hook script to validate Python files before/after editing
# Can be used with PreToolUse or PostToolUse hooks

set -e

# Read the JSON input from stdin
json_input=$(cat)

# Extract relevant information
tool_name=$(echo "$json_input" | jq -r '.tool_name // empty')
file_path=$(echo "$json_input" | jq -r '.tool_args.file_path // empty')

# Only process Python files
if [[ ! "$file_path" =~ \.py$ ]]; then
    exit 0
fi

# Check if file exists
if [[ ! -f "$file_path" ]]; then
    echo "File not found: $file_path" >&2
    exit 0
fi

# Run validation checks
echo "🔍 Validating Python file: $file_path"

# Check for common issues
if grep -q "print(" "$file_path" && [[ ! "$file_path" =~ test_ ]]; then
    echo "⚠️  Warning: Found print() statements in non-test file"
fi

if grep -q "import pdb\|pdb.set_trace" "$file_path"; then
    echo "❌ Error: Found pdb debugger statements"
    exit 1
fi

if grep -q "# TODO\|# FIXME" "$file_path"; then
    echo "📝 Note: Found TODO/FIXME comments"
fi

# Run type checking if in backend directory
if [[ "$file_path" =~ backend/ ]]; then
    cd backend
    if command -v uv &> /dev/null; then
        echo "Running type check..."
        uv run mypy "$file_path" --ignore-missing-imports || true
    fi
fi

echo "✅ Validation complete"

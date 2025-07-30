#!/bin/bash
# Hook script to run tests automatically when test files are modified
# Use with PostToolUse hook

set -e

# Read JSON input
json_input=$(cat)

# Extract file path
file_path=$(echo "$json_input" | jq -r '.tool_args.file_path // empty')

# Check if it's a test file
if [[ "$file_path" =~ test_.*\.py$ ]] || [[ "$file_path" =~ .*\.test\.(ts|tsx|js|jsx)$ ]] || [[ "$file_path" =~ .*\.spec\.(ts|tsx|js|jsx)$ ]]; then
    echo "🧪 Test file modified: $file_path"

    if [[ "$file_path" =~ \.py$ ]]; then
        # Python test
        echo "Running Python test..."
        cd backend
        uv run pytest "$file_path" -v || {
            echo "❌ Test failed!"
            exit 1
        }
    elif [[ "$file_path" =~ \.(ts|tsx|js|jsx)$ ]]; then
        # JavaScript/TypeScript test
        if [[ "$file_path" =~ e2e ]]; then
            echo "E2E test detected - skipping auto-run (use 'npm run test:e2e' manually)"
        else
            echo "Running JavaScript test..."
            cd frontend
            npm test -- "$file_path" || {
                echo "❌ Test failed!"
                exit 1
            }
        fi
    fi

    echo "✅ Test passed!"
fi

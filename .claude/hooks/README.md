# Claude Code Hooks

This directory contains example hook scripts that enhance your development workflow with Claude Code.

## 🪝 What are Hooks?

Claude Code hooks are shell commands that execute at specific points during Claude's operation:

- **PreToolUse**: Before a tool is used (can block operations)
- **PostToolUse**: After a tool completes successfully
- **UserPromptSubmit**: When you submit a prompt
- **Stop**: When Claude finishes responding
- **Notification**: When Claude sends notifications

## 📁 Included Hooks

### validate-python.sh

Validates Python files for common issues:

- Checks for `print()` statements in non-test files
- Detects `pdb` debugger statements
- Finds TODO/FIXME comments
- Runs type checking with mypy

### test-on-save.sh

Automatically runs tests when test files are modified:

- Python tests with pytest
- JavaScript/TypeScript tests
- Skips E2E tests (manual run required)

### security-check.sh

Security validation for dangerous operations:

- Blocks dangerous bash commands (`rm -rf`, etc.)
- Detects hardcoded secrets and API keys
- Validates Django settings
- Warns about sudo usage

### git-auto-stage.sh

Automatically stages modified files to git:

- Stages files after Write/Edit operations
- Respects .gitignore
- Shows staged changes count

## 🚀 Usage

### Option 1: Use the Default Settings

The `.claude/settings.json` already includes basic hooks for:

- Python/TypeScript formatting after edits
- Django model change notifications
- Dangerous command prevention
- Git status on prompt submission

### Option 2: Customize Hooks

1. Copy `.claude/settings.json` to `.claude/settings.local.json`
2. Modify hooks to use the scripts in this directory:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/validate-python.sh"
          }
        ]
      }
    ]
  }
}
```

### Option 3: Create Your Own Hooks

1. Create a new script in this directory
2. Make it executable: `chmod +x your-hook.sh`
3. Add it to your settings file

## 🔧 Hook Script Template

```bash
#!/bin/bash
set -e

# Read JSON input from Claude
json_input=$(cat)

# Extract information
tool_name=$(echo "$json_input" | jq -r '.tool_name // empty')
file_path=$(echo "$json_input" | jq -r '.tool_args.file_path // empty')

# Your logic here
echo "Processing $tool_name on $file_path"

# Exit codes:
# 0 - Success, continue normally
# 1 - Error, show output to user
# 2 - Block operation (PreToolUse only)
```

## 📝 Available Environment Variables

When hooks run, Claude provides:

- `CLAUDE_TOOL_NAME`: The tool being used
- `CLAUDE_TOOL_FILE_PATH`: File being modified (if applicable)
- `CLAUDE_TOOL_COMMAND`: Command being run (for Bash tool)
- `CLAUDE_SESSION_ID`: Current session identifier

## ⚡ Best Practices

1. **Keep hooks fast**: They run synchronously and can slow down Claude
2. **Use `run_in_background: true`** for slow operations like tests
3. **Be selective with matchers**: Don't run hooks on every operation
4. **Handle errors gracefully**: Use proper exit codes
5. **Test hooks thoroughly**: They can block Claude's operations

## 🎯 Common Use Cases

### Development Workflow

- Format code on save
- Run linters automatically
- Check for code smells
- Validate imports

### Security

- Prevent accidental deletions
- Block dangerous commands
- Check for exposed secrets
- Validate permissions

### Testing

- Run unit tests on file changes
- Validate test coverage
- Check for broken imports
- Ensure fixtures are updated

### Git Integration

- Auto-stage changes
- Create atomic commits
- Update branch protection
- Sync with remote

## 🐛 Debugging Hooks

1. Test hooks manually:

   ```bash
   echo '{"tool_name":"Edit","tool_args":{"file_path":"test.py"}}' | .claude/hooks/validate-python.sh
   ```

2. Check Claude's output for hook errors

3. Use `settings.local.json` for testing without affecting team

4. Add debug logging:

   ```bash
   echo "Debug: $json_input" >> /tmp/claude-hook.log
   ```

## 📚 Resources

- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Hook Examples](https://github.com/anthropics/claude-code-examples)
- [Settings Reference](https://docs.anthropic.com/en/docs/claude-code/settings)

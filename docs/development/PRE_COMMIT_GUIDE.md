# Pre-commit Hooks Guide

This project uses [pre-commit](https://pre-commit.com/) to maintain code quality and consistency across the codebase.

## 🚀 Quick Start

```bash
# Install pre-commit (using uv)
uv tool install pre-commit

# Install the git hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

## 📋 Included Hooks

### Python (Backend)

- **Ruff** - Fast Python linter and formatter (replaces Black, isort, flake8, and more)
  - Automatically fixes import sorting, formatting issues
  - Checks for common Python anti-patterns

- **mypy** - Static type checking
  - Ensures type hints are correct
  - Catches type-related bugs before runtime

- **django-upgrade** - Automatically upgrades Django code to newer versions
  - Keeps Django code modern and following best practices

### JavaScript/TypeScript (Frontend)

- **Biome** - Modern, fast linter and formatter (35x faster than ESLint + Prettier)
  - Formats code consistently
  - Catches common bugs and anti-patterns
  - Enforces accessibility best practices
  - No console.log statements in production code

- **TypeScript Check** - Ensures TypeScript code compiles without errors

### Security

- **detect-secrets** - Prevents accidental commit of secrets
  - Scans for API keys, passwords, tokens
  - Use `# pragma: allowlist secret` for false positives

### Documentation

- **markdownlint** - Ensures consistent markdown formatting
  - Auto-fixes common issues
  - Enforces consistent heading styles

### General

- **check-yaml** - Validates YAML syntax
- **check-json** - Validates JSON syntax with auto-formatting
- **check-toml** - Validates TOML files
- **trailing-whitespace** - Removes trailing whitespace
- **end-of-file-fixer** - Ensures files end with newline
- **mixed-line-ending** - Prevents mixed line endings
- **check-merge-conflict** - Prevents committing merge conflicts
- **check-added-large-files** - Warns about large files (default: 500KB)

### Docker

- **hadolint** - Dockerfile linter
  - Requires Docker daemon to be running
  - Skip with `SKIP=hadolint-docker git commit`

## 💡 Common Commands

### Run specific hooks

```bash
# Run only Python hooks
pre-commit run ruff --all-files
pre-commit run mypy --all-files

# Run only frontend hooks
pre-commit run biome-check --all-files

# Run only on staged files (default behavior)
pre-commit run
```

### Update hooks to latest versions

```bash
pre-commit autoupdate
```

### Skip hooks temporarily

```bash
# Skip all hooks (emergency use only!)
git commit --no-verify -m "Emergency fix"

# Skip specific hooks
SKIP=mypy,hadolint-docker git commit -m "Quick fix"
```

### Uninstall hooks

```bash
pre-commit uninstall
```

## 🔧 Configuration

The configuration is in `.pre-commit-config.yaml`. Each hook can be customized:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.6.8
  hooks:
    - id: ruff
      args: [--fix, --exit-non-zero-on-fix]
```

### Adding new hooks

1. Find hooks at [pre-commit.com/hooks](https://pre-commit.com/hooks.html)
2. Add to `.pre-commit-config.yaml`
3. Run `pre-commit install --install-hooks`

## 🐛 Troubleshooting

### "Docker daemon not running"

The hadolint hook requires Docker. Either:

- Start Docker Desktop, or
- Skip the hook: `SKIP=hadolint-docker git commit`

### "Secrets detected"

If you get a false positive:

1. Review the detection to ensure it's not a real secret
2. Add `# pragma: allowlist secret` to the line
3. Never commit real secrets!

### Hook is taking too long

Some hooks like mypy can be slow on first run. They cache results for subsequent runs.

### Biome vs ESLint/Prettier

We use Biome instead of ESLint + Prettier because:

- 35x faster performance
- Single tool instead of multiple
- Better error messages
- Built-in formatting

## 📚 Hook-Specific Guides

### Ruff Configuration

Located in `pyproject.toml`:

```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP", "ARG", "SIM", "TID", "RUF"]
```

### Biome Configuration

Located in `frontend/biome.json`:

- Enforces single quotes in JS/TS
- Double quotes in JSX
- 2-space indentation
- No semicolons (Next.js style)

### Secret Detection

Common patterns it catches:

- AWS keys
- API tokens
- Database URLs with passwords
- Private keys

## 🤝 Contributing

When adding new tools or frameworks:

1. Add appropriate pre-commit hooks
2. Document any new hooks in this guide
3. Test hooks work correctly with `pre-commit run --all-files`

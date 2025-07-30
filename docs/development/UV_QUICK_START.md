# Getting Started with UV

> **uv** is an extremely fast Python package and project manager, written in Rust. It's 10-100x faster than pip and handles everything from Python installation to dependency management.

## Why UV?

- **⚡ Lightning Fast**: 10-100x faster than pip
- **🔒 Reliable**: Proper dependency resolution with lockfiles
- **🐍 Python Management**: Install and manage Python versions
- **📦 All-in-One**: Replaces pip, pip-tools, pipenv, poetry, pyenv, virtualenv
- **🔧 Drop-in Replacement**: Works with existing requirements.txt and pyproject.toml

## Installation

### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### With Homebrew

```bash
brew install uv
```

## Basic Usage

### Python Management

```bash
# Install Python (if needed)
uv python install 3.12

# List available Python versions
uv python list

# Use specific Python version
uv python pin 3.12
```

### Project Setup

```bash
# Create new project
uv init my-project
cd my-project

# Or use existing project
cd existing-project
uv sync  # Install dependencies from pyproject.toml
```

### Dependency Management

```bash
# Add a dependency
uv add django
uv add "django>=5.0"
uv add django-ninja pydantic

# Add dev dependency
uv add --dev pytest ruff mypy

# Remove dependency
uv remove django-old-package

# Update dependencies
uv lock --upgrade-package django
uv sync  # Apply updates
```

### Running Commands

```bash
# Run commands in the virtual environment
uv run python manage.py runserver
uv run pytest
uv run ruff check .

# Or activate the environment
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
```

### Installing from requirements.txt

```bash
# Install from requirements.txt
uv pip install -r requirements.txt

# Generate requirements.txt from lock file
uv pip compile pyproject.toml -o requirements.txt
```

## UV with This Template

### Backend Setup

```bash
cd backend

# Install all dependencies
uv sync

# Run Django commands
uv run python manage.py migrate
uv run python manage.py runserver

# Run tests
uv run pytest

# Run linting
uv run ruff check .
uv run ruff format .
```

### Tool Installation

UV can also install Python CLI tools globally:

```bash
# Install pre-commit with uv acceleration
uv tool install pre-commit --with pre-commit-uv

# Install other tools
uv tool install ruff
uv tool install mypy

# List installed tools
uv tool list

# Run tools
uvx ruff check .  # Run without installing
```

## Lock Files

### Understanding uv.lock

- **uv.lock** ensures everyone uses exact same dependency versions
- Always commit uv.lock to version control
- Automatically updated when you add/remove dependencies

### Syncing Dependencies

```bash
# Install exact versions from lock file
uv sync

# Update lock file with latest compatible versions
uv lock --upgrade

# Update specific package
uv lock --upgrade-package django
```

## Integration with IDEs

### VS Code

1. UV creates virtual environment at `.venv`
2. VS Code should auto-detect it
3. If not, select interpreter: `Cmd/Ctrl + Shift + P` → "Python: Select Interpreter" → `.venv/bin/python`

### PyCharm

1. Go to Settings → Project → Python Interpreter
2. Add Interpreter → Existing Environment
3. Select `.venv/bin/python`

## Common Workflows

### Starting Fresh

```bash
# Clone the template
git clone <template-url>
cd ai-project-template/backend

# Install dependencies
uv sync

# Run the project
uv run python manage.py migrate
uv run python manage.py runserver
```

### Adding New Features

```bash
# Add new package
uv add django-cors-headers

# Sync to install
uv sync

# Commit the lock file
git add pyproject.toml uv.lock
git commit -m "Add django-cors-headers"
```

### CI/CD with UV

```yaml
# GitHub Actions example
- name: Install uv
  uses: astral-sh/setup-uv@v4

- name: Install dependencies
  run: uv sync

- name: Run tests
  run: uv run pytest
```

## Performance Tips

1. **Use `uv sync` not `uv pip install`** for better performance
2. **Enable pre-commit-uv** for faster git hooks:

   ```bash
   uv tool install pre-commit --with pre-commit-uv
   ```

3. **Cache in CI**: UV caches packages globally, speeding up CI builds

## Troubleshooting

### "Command not found: uv"

Add UV to your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Python version issues

```bash
# Install required Python version
uv python install 3.12

# Pin to project
uv python pin 3.12
```

### Dependency conflicts

```bash
# See why a package is included
uv tree

# Force reinstall all dependencies
uv sync --reinstall
```

## Migrating from pip/poetry

### From pip

```bash
# Convert requirements.txt to pyproject.toml
uv add $(cat requirements.txt)
```

### From poetry

```bash
# UV reads pyproject.toml directly
uv sync
```

## Further Reading

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Astral Blog](https://astral.sh/blog)

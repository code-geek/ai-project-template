# AI Project Template 🚀

> **A comprehensive Django + Next.js template optimized for AI-assisted development**

This template provides a modern, production-ready foundation for building full-stack applications with Django and Next.js. It's specifically designed to work seamlessly with AI coding assistants like Claude, featuring specialized agents, clear documentation structure, and best practices baked in.

## ✨ Why Use This Template?

- **🤖 AI-Optimized**: Includes Claude Code agents and CLAUDE.md files for enhanced AI assistance
- **🏗️ Modern Stack**: Django 5.1 + Django Ninja backend, Next.js 15 + TypeScript frontend
- **🚀 Production-Ready**: Docker, CI/CD workflows, and deployment scripts included
- **📚 Well-Documented**: Comprehensive docs and inline guidance for easy customization
- **🧪 Testing Built-in**: Pytest for backend, Playwright for E2E, with example tests
- **🎨 Beautiful UI**: Tailwind CSS + shadcn/ui components pre-configured
- **🔧 Code Quality**: Pre-commit hooks, Ruff linting, mypy type checking
- **⚡ Fast Tooling**: Uses uv for 10-100x faster Python package management

## 🚀 Quick Start

### Using This Template

1. **Create your repository from this template:**

   ```bash
   # Using GitHub CLI
   gh repo create my-project --template code-geek/ai-project-template --public

   # Or use the GitHub web interface:
   # Click "Use this template" button on GitHub
   ```

2. **Clone and setup your new project:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/my-project
   cd my-project

   # Run the setup script
   ./scripts/setup-dev.sh
   ```

3. **Start developing:**

   ```bash
   # Using Docker (recommended)
   docker-compose up

   # Or run separately
   cd backend && uv run python manage.py runserver
   cd frontend && npm run dev
   ```

   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000/api/docs>

## 🏗️ Tech Stack

### Backend

- **Framework**: Python 3.12 + Django 5.1 + Django Ninja
- **Database**: PostgreSQL 16 (SQLite for dev)
- **Caching**: Redis
- **Task Queue**: Celery (optional)

### Frontend

- **Framework**: Next.js 15 (App Router) + React 19
- **Language**: TypeScript 5.x
- **Styling**: Tailwind CSS + shadcn/ui
- **State**: Zustand / React Context

### Infrastructure

- **Containers**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Deployment**: AWS ECS/EC2 or Vercel
- **Monitoring**: Sentry (optional)

## 🎨 Customization Guide

### 1. Update Project Information

- Replace `Project Name` with your project name throughout
- Update `package.json` and `pyproject.toml` with your project details
- Modify `CLAUDE.md` files to reflect your project's specific needs

### 2. Configure Environment

- Copy `.env.example` files and update with your settings
- Update `ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS` in Django settings
- Set your `NEXT_PUBLIC_API_URL` in frontend `.env.local`

### 3. Customize the Stack

- **Remove Celery**: Delete celery services from `docker-compose.yml` if not needed
- **Add Authentication**: Implement your preferred auth method (JWT included)
- **Database**: Switch from PostgreSQL to MySQL/MongoDB if preferred
- **Styling**: Replace Tailwind with styled-components/emotion if desired

### 4. Update CI/CD

- Modify `.github/workflows/` to match your deployment target
- Update branch names if not using `main` and `production`
- Add your secrets to GitHub repository settings

## 🤖 Claude Code Agents

This template includes specialized AI agents in `.claude/agents/`:

- **code-reviewer**: Reviews code for quality and security
- **test-writer**: Writes comprehensive tests
- **backend-architect**: Designs Django REST APIs
- **frontend-engineer**: Builds React/Next.js features
- **debugger**: Systematically resolves errors
- **performance-optimizer**: Improves speed and efficiency
- **api-designer**: Creates RESTful API specifications

Agents activate automatically based on context or can be requested explicitly.

## 📁 Project Structure

```plaintext
.
├── .claude/          # AI assistant configuration
│   └── agents/      # Specialized AI agents
├── backend/          # Django REST API
│   ├── apps/        # Django applications
│   ├── config/      # Settings and configuration
│   └── tests/       # Test files
├── frontend/         # Next.js application
│   ├── src/         # Source code
│   │   ├── app/     # App Router pages
│   │   └── components/ # React components
│   └── tests/       # Test files
├── docs/            # Documentation
├── scripts/         # Utility scripts
└── docker-compose.yml
```

## 🛠️ Development

### Prerequisites

- Python 3.12+
- Node.js 20+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Backend Development

```bash
cd backend
uv sync                          # Install dependencies
cp .env.example .env             # Configure environment
uv run python manage.py migrate  # Setup database
uv run python manage.py runserver # Start server (localhost:8000)
```

### Frontend Development

```bash
cd frontend
npm install                      # Install dependencies
cp .env.example .env.local       # Configure environment
npm run dev                      # Start dev server (localhost:3000)
```

### Code Quality & Pre-commit Hooks

This template includes comprehensive pre-commit hooks for maintaining code quality:

```bash
# Install pre-commit hooks (one-time setup)
uv tool install pre-commit
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Skip specific hooks if needed (e.g., Docker when daemon not running)
SKIP=hadolint-docker git commit -m "your message"
```

**Included hooks:**

- **Python**: Ruff (linting/formatting), mypy (type checking), django-upgrade
- **Frontend**: Biome (fast ESLint + Prettier replacement), TypeScript checking
- **Security**: Secret detection, security patterns
- **General**: YAML/JSON validation, trailing whitespace, file endings
- **Documentation**: Markdownlint
- **Docker**: Hadolint (requires Docker daemon)

### Running Tests

```bash
# Backend tests
cd backend && uv run pytest

# Frontend tests
cd frontend && npm run test:e2e

# Run all tests
./scripts/run-tests.sh
```

## 🚢 Deployment

### Using Docker

```bash
# Build and run production containers
docker-compose -f docker-compose.prod.yml up --build
```

### Deploy to AWS

```bash
# Configure AWS credentials
aws configure

# Deploy using the script
./scripts/deploy.sh production
```

See [deployment guide](docs/deployment/AWS_DEPLOYMENT.md) for detailed instructions.

## 📚 Documentation

- [Developer Quick Start](docs/development/DEVELOPER_QUICK_START.md)
- [Architecture Overview](docs/development/ARCHITECTURE.md)
- [API Documentation](http://localhost:8000/api/docs)
- [Contributing Guide](CONTRIBUTING.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django Ninja](https://django-ninja.dev/) for the amazing API framework
- [shadcn/ui](https://ui.shadcn.com/) for beautiful components
- [Next.js](https://nextjs.org/) for the React framework

---

## 📖 Template Documentation

- [How to Use This Template](docs/TEMPLATE_USAGE.md)
- [Customization Examples](docs/CUSTOMIZATION_EXAMPLES.md)
- [Deployment Options](docs/deployment/)
- [Adding New Features](docs/ADDING_FEATURES.md)

---

**Need help?** [Open an issue](https://github.com/code-geek/ai-project-template/issues) or check the [documentation](docs/).

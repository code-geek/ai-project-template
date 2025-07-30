# Developer Quick Start Guide

Get up and running with the project in under 10 minutes!

## Prerequisites

- Python 3.12+
- Node.js 20+
- Docker & Docker Compose
- Git

## Quick Setup

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repo-url>
cd project-name

# Create a new branch for your work
git checkout -b feature/your-feature-name
```

### 2. Environment Setup

```bash
# Backend environment
cd backend
cp .env.example .env
# Edit .env with your settings

# Frontend environment
cd ../frontend
cp .env.example .env.local
# Edit .env.local with your settings
```

### 3. Start with Docker (Recommended)

```bash
# From project root
docker-compose up

# Services will be available at:
# - Frontend: http://localhost:3000
# - Backend API: http://localhost:8000
# - API Docs: http://localhost:8000/api/docs
# - PostgreSQL: localhost:5432
# - Redis: localhost:6379
```

### 4. Manual Setup (Alternative)

#### Backend
```bash
cd backend

# Install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Run migrations
uv run python manage.py migrate

# Create superuser (optional)
uv run python manage.py createsuperuser

# Start server
uv run python manage.py runserver
```

#### Frontend
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## Common Development Tasks

### Running Tests

```bash
# Backend tests
cd backend && uv run pytest

# Frontend tests
cd frontend && npm run test:e2e

# Run all tests
./scripts/run-tests.sh
```

### Code Quality

```bash
# Backend
cd backend
uv run ruff check .  # Linting
uv run mypy .        # Type checking

# Frontend
cd frontend
npm run lint         # ESLint
npm run type-check   # TypeScript
npm run format       # Prettier
```

### Database Operations

```bash
# Create new migration
cd backend
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Reset database
uv run python manage.py flush
```

### Adding Dependencies

```bash
# Backend
cd backend
uv add package-name

# Frontend
cd frontend
npm install package-name
```

## Project Structure Overview

```
.
├── backend/
│   ├── apps/          # Django apps
│   ├── config/        # Settings & URLs
│   └── tests/         # Tests
├── frontend/
│   ├── src/
│   │   ├── app/       # Next.js pages
│   │   ├── components/ # React components
│   │   └── lib/       # Utilities
│   └── tests/         # E2E tests
└── docs/              # Documentation
```

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### Docker Issues
```bash
# Clean rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

### Database Connection Issues
```bash
# Check if PostgreSQL is running
docker-compose ps postgres

# Check logs
docker-compose logs postgres
```

## Next Steps

1. Read the [Architecture Overview](ARCHITECTURE.md)
2. Check out existing [API Documentation](http://localhost:8000/api/docs)
3. Review the [Contributing Guide](../../CONTRIBUTING.md)
4. Start working on your feature!

## Getting Help

- Check the [FAQ](../FAQ.md)
- Search existing [Issues](https://github.com/username/project/issues)
- Ask in the project chat/discord
- Create a new issue with the `question` label
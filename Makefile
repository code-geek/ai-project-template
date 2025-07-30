# Makefile for AI Project Template
.PHONY: help install dev test lint format clean build deploy

# Default target
help:
	@echo "Available commands:"
	@echo "  make install      Install all dependencies"
	@echo "  make dev          Start development servers"
	@echo "  make test         Run all tests"
	@echo "  make lint         Run linters"
	@echo "  make format       Format code"
	@echo "  make clean        Clean up generated files"
	@echo "  make build        Build for production"
	@echo "  make deploy       Deploy to production"

# Installation
install:
	@echo "📦 Installing dependencies..."
	@echo "Backend..."
	cd backend && uv sync
	@echo "Frontend..."
	cd frontend && npm install
	@echo "Pre-commit hooks..."
	uv tool install pre-commit
	pre-commit install
	@echo "✅ Installation complete!"

# Development
dev:
	@echo "🚀 Starting development servers..."
	docker-compose up

dev-backend:
	cd backend && uv run python manage.py runserver

dev-frontend:
	cd frontend && npm run dev

# Database
db-migrate:
	cd backend && uv run python manage.py makemigrations
	cd backend && uv run python manage.py migrate

db-reset:
	cd backend && uv run python manage.py flush --no-input
	cd backend && uv run python manage.py migrate

db-seed:
	cd backend && uv run python manage.py loaddata fixtures/initial_data.json

# Testing
test: test-backend test-frontend

test-backend:
	@echo "🧪 Running backend tests..."
	cd backend && uv run pytest

test-frontend:
	@echo "🧪 Running frontend tests..."
	cd frontend && npm run test:e2e

test-watch:
	cd backend && uv run ptw

# Code quality
lint: lint-backend lint-frontend

lint-backend:
	@echo "🔍 Linting backend..."
	cd backend && uv run ruff check .

lint-frontend:
	@echo "🔍 Linting frontend..."
	cd frontend && npm run lint:check

format: format-backend format-frontend

format-backend:
	@echo "✨ Formatting backend..."
	cd backend && uv run ruff format .
	cd backend && uv run ruff check --fix .

format-frontend:
	@echo "✨ Formatting frontend..."
	cd frontend && npm run lint

type-check:
	@echo "🔍 Type checking..."
	cd backend && uv run mypy .
	cd frontend && npm run type-check

# Pre-commit
pre-commit:
	pre-commit run --all-files

pre-commit-update:
	pre-commit autoupdate

# Docker
docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-shell-backend:
	docker-compose exec backend bash

docker-shell-frontend:
	docker-compose exec frontend sh

# Production
build: build-backend build-frontend

build-backend:
	@echo "🏗️ Building backend..."
	cd backend && uv run python manage.py collectstatic --noinput
	cd backend && uv build

build-frontend:
	@echo "🏗️ Building frontend..."
	cd frontend && npm run build

deploy-check:
	@echo "🔍 Running deployment checks..."
	cd backend && uv run python manage.py check --deploy
	@echo "✅ Deployment checks passed!"

# Cleanup
clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".DS_Store" -delete
	rm -rf backend/staticfiles
	rm -rf frontend/.next
	rm -rf frontend/out
	rm -rf coverage
	rm -rf htmlcov
	@echo "✨ Clean complete!"

# Environment
env-check:
	@echo "🔍 Checking environment variables..."
	@test -f backend/.env || (echo "❌ backend/.env not found" && exit 1)
	@test -f frontend/.env.local || (echo "❌ frontend/.env.local not found" && exit 1)
	@echo "✅ Environment files present!"

# Database management
db-backup:
	@echo "💾 Backing up database..."
	@mkdir -p backups
	@docker-compose exec postgres pg_dump -U postgres projectdb > backups/backup_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "✅ Backup complete!"

db-restore:
	@echo "📥 Restoring database from latest backup..."
	@docker-compose exec -T postgres psql -U postgres projectdb < $(shell ls -t backups/*.sql | head -1)
	@echo "✅ Restore complete!"

# Shortcuts
i: install
d: dev
t: test
l: lint
f: format

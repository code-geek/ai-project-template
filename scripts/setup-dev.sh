#!/bin/bash

# Development Environment Setup Script

set -e  # Exit on error

echo "🚀 Setting up development environment..."

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required but not installed. Aborting." >&2; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required but not installed. Aborting." >&2; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed. Aborting." >&2; exit 1; }

# Setup backend
echo "
🔧 Setting up backend..."
cd backend

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Please update backend/.env with your configuration"
fi

# Install dependencies
uv sync

# Setup frontend
echo "
🎨 Setting up frontend..."
cd ../frontend

# Copy environment file
if [ ! -f .env.local ]; then
    cp .env.example .env.local
    echo "⚠️  Please update frontend/.env.local with your configuration"
fi

# Install dependencies
npm install

# Back to root
cd ..

# Start services
echo "
🔥 Starting services with Docker Compose..."
docker-compose up -d postgres redis

echo "
✅ Setup complete!"
echo "
Next steps:"
echo "1. Update environment files if needed"
echo "2. Run 'docker-compose up' to start all services"
echo "3. Visit http://localhost:3000 for frontend"
echo "4. Visit http://localhost:8000/api/docs for API docs"
echo "
Happy coding! 🎉"
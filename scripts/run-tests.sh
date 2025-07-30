#!/bin/bash

# Run all project tests

set -e  # Exit on error

echo "🧪 Running all tests..."

# Backend tests
echo "
🔧 Running backend tests..."
cd backend
uv run pytest -v --cov=apps --cov-report=term-missing

# Frontend tests
echo "
🎨 Running frontend tests..."
cd ../frontend
npm run lint
npm run type-check
npm run test:e2e

echo "
✅ All tests passed!"
# 🤖 AI Assistant Instructions

> **Note**: This is a template repository. When using this template for your own project, customize this file to match your specific workflow and requirements.

## 📋 User's Preferred Workflow

1. Think through problem, read codebase, write plan to docs/project_management/TODO.md
2. Create todo list with checkable items
3. Check in with user before starting
4. Work on todos, marking complete as you go
5. Give high-level explanations only
6. Keep changes simple and minimal
7. Add review section to TODO.md when done

## 🎯 Important Rules

- **No comments in code** unless explicitly asked
- **Always use TodoWrite tool** to track progress
- **Test all changes** before marking complete
- **Run linting/formatting** after code changes
- **Commit only when explicitly asked**

## 🏗️ Project Structure

- **Backend**: Django REST API with Django Ninja
- **Frontend**: Next.js with TypeScript and Tailwind CSS
- **Database**: PostgreSQL (dev: SQLite)
- **Testing**: pytest (backend), Playwright (e2e)
- **Deployment**: Docker + AWS (ECS/EC2)

## 🗂️ Key Locations

- **Backend API**: `backend/apps/*/api.py` (Django Ninja endpoints)
- **Models**: `backend/apps/*/models.py`
- **Services**: `backend/apps/*/services.py` (business logic)
- **Frontend Pages**: `frontend/src/app/` (App Router)
- **Components**: `frontend/src/components/`
- **API Client**: `frontend/src/lib/api.ts`
- **Types**: `frontend/src/types/`
- **Tests**: `backend/tests/`, `frontend/tests/e2e/`

## 🔧 Common Commands

### Backend
```bash
cd backend
uv sync                           # Install dependencies
uv run python manage.py migrate   # Run migrations
uv run python manage.py runserver # Start dev server
uv run pytest                     # Run tests
uv run ruff check .              # Lint code
```

### Frontend
```bash
cd frontend
npm install                      # Install dependencies
npm run dev                      # Start dev server
npm run build                    # Build for production
npm run test:e2e                 # Run E2E tests
npm run lint                     # Lint code
npm run type-check              # TypeScript check
```

## 🚀 Development Workflow

1. **Feature Development**:
   - Create feature branch
   - Update TODO.md with plan
   - Implement backend API first
   - Create frontend UI
   - Write tests
   - Update documentation

2. **Testing Strategy**:
   - Unit tests for services
   - Integration tests for APIs
   - E2E tests for critical flows
   - Always run tests before completion

3. **Code Style**:
   - Follow existing patterns
   - Use type hints (Python)
   - Use TypeScript strictly
   - Prefer composition over inheritance

## 📝 Documentation

- Update README for major features
- Keep API documentation current
- Document complex business logic
- Add examples for new patterns

## 🔒 Security Notes

- Never commit secrets or API keys
- Use environment variables
- Validate all user inputs
- Follow OWASP guidelines
# Backend API

Django REST API built with Django Ninja for high-performance, type-safe endpoints.

## Quick Start

```bash
# Install dependencies with uv
uv sync

# Set up environment
cp .env.example .env

# Run migrations
uv run python manage.py migrate

# Create superuser (optional)
uv run python manage.py createsuperuser

# Start development server
uv run python manage.py runserver
```

API will be available at <http://localhost:8000/api/docs>

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=apps --cov-report=html

# Run specific test
uv run pytest apps/users/tests/test_api.py::TestUserAPI::test_create_user
```

### Code Quality

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check . --fix

# Type checking
uv run mypy .
```

### Database Commands

```bash
# Create migrations
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# Reset database
uv run python manage.py flush
```

## Project Structure

```plaintext
apps/
├── core/          # Shared utilities and base classes
├── users/         # User management and authentication
└── <feature>/     # Feature-specific apps
    ├── api.py     # Django Ninja endpoints
    ├── models.py  # Database models
    ├── schemas.py # Pydantic schemas
    ├── services.py # Business logic
    └── tests/     # App tests
```

## API Documentation

- Swagger UI: <http://localhost:8000/api/docs>
- ReDoc: <http://localhost:8000/api/redoc>
- OpenAPI Schema: <http://localhost:8000/api/openapi.json>

## Environment Variables

See `.env.example` for required environment variables.

Key variables:

- `DEBUG`: Set to False in production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Adding New Features

1. Create new app:

   ```bash
   cd apps
   mkdir new_feature
   cd new_feature
   touch __init__.py models.py api.py schemas.py services.py
   ```

2. Add to `INSTALLED_APPS` in `config/settings.py`

3. Create API endpoints in `api.py`

4. Register router in `config/urls.py`

5. Write tests in `tests/`

## Production Deployment

For production deployment, use gunicorn:

```bash
uv run gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

See the main [deployment guide](../docs/deployment/AWS_DEPLOYMENT.md) for full instructions.

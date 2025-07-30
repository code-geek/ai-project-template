# Backend AI Instructions

## 🏗️ Backend Architecture

- **Framework**: Django 5.1 with Django Ninja for APIs
- **Database**: PostgreSQL (SQLite in dev)
- **Authentication**: JWT tokens
- **API Style**: RESTful with OpenAPI schema

## 📁 App Structure

```plaintext
apps/
├── core/          # Shared utilities, base models
├── users/         # User management, auth
└── <feature>/     # Feature-specific apps
    ├── api.py     # Django Ninja endpoints
    ├── models.py  # Django models
    ├── schemas.py # Pydantic schemas
    ├── services.py # Business logic
    └── tests/     # App tests
```

## 📝 API Patterns

### Django Ninja Router

```python
from ninja import Router
from .schemas import ItemIn, ItemOut
from .services import ItemService

router = Router()

@router.post("/", response=ItemOut)
def create_item(request, data: ItemIn):
    return ItemService.create(data.dict())

@router.get("/{item_id}", response=ItemOut)
def get_item(request, item_id: int):
    return ItemService.get(item_id)
```

### Service Layer

```python
from .models import Item

class ItemService:
    @staticmethod
    def create(data: dict) -> Item:
        return Item.objects.create(**data)

    @staticmethod
    def get(item_id: int) -> Item:
        return Item.objects.get(id=item_id)
```

## 🔧 Common Tasks

### Add New App

```bash
cd backend/apps
mkdir new_feature
cd new_feature
touch __init__.py api.py models.py schemas.py services.py
mkdir tests
touch tests/__init__.py tests/test_api.py
```

### Run Migrations

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

### Testing

```bash
# Run all tests
uv run pytest

# Run specific app tests
uv run pytest apps/users/tests/

# With coverage
uv run pytest --cov=apps --cov-report=html
```

## 🛡️ Security

- Always validate input with Pydantic schemas
- Use Django's ORM to prevent SQL injection
- Implement proper permission classes
- Never expose sensitive data in API responses

## 📦 Dependencies

Add new dependencies to `pyproject.toml`:

```bash
uv add package-name
```

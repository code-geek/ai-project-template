"""
Shared pytest fixtures for all tests.
"""

import pytest
from django.contrib.auth import get_user_model
from ninja.testing import TestClient

from apps.users.models import User as UserType

User = get_user_model()


@pytest.fixture
def api_client():
    """Create a test client for API testing."""
    from config.api_config import api

    return TestClient(api)


@pytest.fixture
def user(db) -> UserType:  # noqa: ARG001
    """Create a test user."""
    return User.objects.create_user(  # type: ignore[attr-defined]
        email="test@example.com",
        password="testpass123",  # pragma: allowlist secret
        first_name="Test",
        last_name="User",
    )


@pytest.fixture
def auth_client(api_client, user):
    """Create an authenticated test client."""
    # In a real app, you'd implement JWT token generation here
    # For now, we'll use a simple session auth
    api_client.force_authenticate(user)
    return api_client


@pytest.fixture
def admin_user(db) -> UserType:  # noqa: ARG001
    """Create an admin user."""
    return User.objects.create_superuser(  # type: ignore[attr-defined]
        email="admin@example.com",
        password="adminpass123",  # pragma: allowlist secret
        first_name="Admin",
        last_name="User",
    )

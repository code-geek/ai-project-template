"""Example API tests to demonstrate testing patterns."""
# ruff: noqa: S101, ANN401, ARG002

from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser
    from django.test import Client

# HTTP status codes as constants
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_401_UNAUTHORIZED = 401


class TestHealthCheck:
    """Test health check endpoints."""

    def test_health_check(self, api_client: "Client") -> None:
        """Test basic health check endpoint."""
        response = api_client.get("/api/health/")
        assert response.status_code == HTTP_200_OK
        assert response.json()["status"] == "healthy"

    def test_db_health_check(self, api_client: "Client", db: Any) -> None:
        """Test database health check."""
        response = api_client.get("/api/health/db/")
        assert response.status_code == HTTP_200_OK
        assert response.json()["database"] == "connected"


class TestUserAPI:
    """Test user-related API endpoints."""

    @pytest.mark.django_db
    def test_user_registration(self, api_client: "Client") -> None:
        """Test user registration endpoint."""
        data = {
            "email": "newuser@example.com",
            "password": "securepass123",  # pragma: allowlist secret
            "first_name": "New",
            "last_name": "User",
        }
        response = api_client.post("/api/auth/register/", json=data)
        assert response.status_code == HTTP_201_CREATED
        assert response.json()["email"] == data["email"]

    @pytest.mark.django_db
    def test_user_login(self, api_client: "Client", user: "AbstractUser") -> None:
        """Test user login endpoint."""
        data = {
            "email": "test@example.com",
            "password": "testpass123",  # pragma: allowlist secret
        }
        response = api_client.post("/api/auth/login/", json=data)
        assert response.status_code == HTTP_200_OK
        assert "access_token" in response.json()

    @pytest.mark.django_db
    def test_get_current_user(
        self, auth_client: "Client", user: "AbstractUser"
    ) -> None:
        """Test getting current user info."""
        response = auth_client.get("/api/auth/me/")
        assert response.status_code == HTTP_200_OK
        assert response.json()["email"] == user.email


class TestProtectedEndpoints:
    """Test authentication requirements."""

    def test_unauthenticated_access(self, api_client: "Client") -> None:
        """Test that protected endpoints require authentication."""
        response = api_client.get("/api/users/profile/")
        assert response.status_code == HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_authenticated_access(self, auth_client: "Client") -> None:
        """Test authenticated access to protected endpoints."""
        response = auth_client.get("/api/users/profile/")
        assert response.status_code == HTTP_200_OK

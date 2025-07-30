"""
Example API tests to demonstrate testing patterns.
"""

import pytest


class TestHealthCheck:
    """Test health check endpoints."""

    def test_health_check(self, api_client):
        """Test basic health check endpoint."""
        response = api_client.get("/api/health/")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_db_health_check(self, api_client, db):  # noqa: ARG002
        """Test database health check."""
        response = api_client.get("/api/health/db/")
        assert response.status_code == 200
        assert response.json()["database"] == "connected"


class TestUserAPI:
    """Test user-related API endpoints."""

    @pytest.mark.django_db
    def test_user_registration(self, api_client):
        """Test user registration endpoint."""
        data = {
            "email": "newuser@example.com",
            "password": "securepass123",  # pragma: allowlist secret
            "first_name": "New",
            "last_name": "User",
        }
        response = api_client.post("/api/auth/register/", json=data)
        assert response.status_code == 201
        assert response.json()["email"] == data["email"]

    @pytest.mark.django_db
    def test_user_login(self, api_client, user):  # noqa: ARG002
        """Test user login endpoint."""
        data = {
            "email": "test@example.com",
            "password": "testpass123",  # pragma: allowlist secret
        }
        response = api_client.post("/api/auth/login/", json=data)
        assert response.status_code == 200
        assert "access_token" in response.json()

    @pytest.mark.django_db
    def test_get_current_user(self, auth_client, user):
        """Test getting current user info."""
        response = auth_client.get("/api/auth/me/")
        assert response.status_code == 200
        assert response.json()["email"] == user.email


class TestProtectedEndpoints:
    """Test authentication requirements."""

    def test_unauthenticated_access(self, api_client):
        """Test that protected endpoints require authentication."""
        response = api_client.get("/api/users/profile/")
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_authenticated_access(self, auth_client):
        """Test authenticated access to protected endpoints."""
        response = auth_client.get("/api/users/profile/")
        assert response.status_code == 200

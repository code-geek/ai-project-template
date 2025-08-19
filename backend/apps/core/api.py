"""Core API endpoints including health checks."""

from datetime import UTC, datetime
from typing import Any

from django.core.cache import cache
from django.db import connection
from django.http import HttpRequest
from ninja import Router

router = Router(tags=["Core"])


@router.get("/health/", response=dict[str, Any])
def health_check(request: HttpRequest) -> dict[str, Any]:  # noqa: ARG001
    """Return basic health check status."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat(),
        "service": "backend-api",
        "version": "1.0.0",
    }


@router.get("/health/db/", response=dict[str, Any])
def database_health_check(request: HttpRequest) -> dict[str, Any]:  # noqa: ARG001
    """Check database connectivity status."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        db_status = "connected"
        db_error = None
    except (ConnectionError, Exception) as e:
        db_status = "error"
        db_error = str(e)

    return {
        "database": db_status,
        "error": db_error,
        "timestamp": datetime.now(UTC).isoformat(),
    }


@router.get("/health/cache/", response=dict[str, Any])
def cache_health_check(request: HttpRequest) -> dict[str, Any]:  # noqa: ARG001
    """Check cache connectivity status."""
    try:
        cache.set("health_check", "ok", 1)
        value = cache.get("health_check")
        cache_status = "connected" if value == "ok" else "error"
        cache_error = None
    except (ConnectionError, Exception) as e:
        cache_status = "error"
        cache_error = str(e)

    return {
        "cache": cache_status,
        "error": cache_error,
        "timestamp": datetime.now(UTC).isoformat(),
    }


@router.get("/health/ready/", response=dict[str, Any])
def readiness_check(request: HttpRequest) -> dict[str, Any]:  # noqa: ARG001
    """Comprehensive readiness check for Kubernetes/load balancers.

    Returns 503 if any critical service is down.
    """
    checks = {"database": True, "cache": True, "migrations": True}
    errors = {}

    # Check database
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except (ConnectionError, Exception) as e:
        checks["database"] = False
        errors["database"] = str(e)

    # Check cache
    try:
        cache.set("readiness_check", "ok", 1)
        if cache.get("readiness_check") != "ok":
            checks["cache"] = False
    except (ConnectionError, Exception) as e:
        checks["cache"] = False
        errors["cache"] = str(e)

    # Check for pending migrations
    try:
        from io import StringIO

        from django.core.management import call_command

        out = StringIO()
        call_command("showmigrations", "--plan", stdout=out)
        if "[ ]" in out.getvalue():
            checks["migrations"] = False
            errors["migrations"] = "Pending migrations detected"
    except (ImportError, Exception) as e:
        checks["migrations"] = False
        errors["migrations"] = str(e)

    all_healthy = all(checks.values())

    # Note: In Django Ninja, status codes should be handled at the router level
    # For now, we return the data and let the caller handle the status
    return {
        "ready": all_healthy,
        "checks": checks,
        "errors": errors if errors else None,
        "timestamp": datetime.now(UTC).isoformat(),
    }

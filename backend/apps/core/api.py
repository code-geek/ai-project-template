"""
Core API endpoints including health checks.
"""

from datetime import datetime
from typing import Any

from django.core.cache import cache
from django.db import connection
from ninja import Router

router = Router(tags=["Core"])


@router.get("/health/", response=dict[str, Any])
def health_check(request) -> dict[str, Any]:  # noqa: ARG001
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "backend-api",
        "version": "1.0.0",
    }


@router.get("/health/db/", response=dict[str, Any])
def database_health_check(request) -> dict[str, Any]:  # noqa: ARG001
    """Check database connectivity."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        db_status = "connected"
        db_error = None
    except Exception as e:
        db_status = "error"
        db_error = str(e)

    return {
        "database": db_status,
        "error": db_error,
        "timestamp": datetime.utcnow().isoformat(),
    }


@router.get("/health/cache/", response=dict[str, Any])
def cache_health_check(request) -> dict[str, Any]:  # noqa: ARG001
    """Check cache connectivity."""
    try:
        cache.set("health_check", "ok", 1)
        value = cache.get("health_check")
        cache_status = "connected" if value == "ok" else "error"
        cache_error = None
    except Exception as e:
        cache_status = "error"
        cache_error = str(e)

    return {
        "cache": cache_status,
        "error": cache_error,
        "timestamp": datetime.utcnow().isoformat(),
    }


@router.get("/health/ready/", response=dict[str, Any])
def readiness_check(request) -> dict[str, Any]:
    """
    Comprehensive readiness check for Kubernetes/load balancers.
    Returns 503 if any critical service is down.
    """
    checks = {"database": True, "cache": True, "migrations": True}
    errors = {}

    # Check database
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception as e:
        checks["database"] = False
        errors["database"] = str(e)

    # Check cache
    try:
        cache.set("readiness_check", "ok", 1)
        if cache.get("readiness_check") != "ok":
            checks["cache"] = False
    except Exception as e:
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
    except Exception as e:
        checks["migrations"] = False
        errors["migrations"] = str(e)

    all_healthy = all(checks.values())

    response_data = {
        "ready": all_healthy,
        "checks": checks,
        "errors": errors if errors else None,
        "timestamp": datetime.utcnow().isoformat(),
    }

    if not all_healthy:
        # Return 503 Service Unavailable if not ready
        request.response.status_code = 503

    return response_data

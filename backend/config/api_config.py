"""
Main API configuration for Django Ninja.
"""

from ninja import NinjaAPI
from ninja.security import HttpBearer

from apps.core.api import router as core_router

# from apps.users.api import router as users_router
# from apps.auth.api import router as auth_router


class AuthBearer(HttpBearer):
    """JWT Bearer token authentication."""

    def authenticate(self, request, token):  # noqa: ARG002
        # TODO: Implement JWT validation
        # For now, just check if token exists
        if token:
            # In production, validate JWT and return user
            return token
        return None


# Create API instance
api = NinjaAPI(
    title="AI Project API",
    version="1.0.0",
    description="RESTful API for AI Project Template",
    docs_url="/docs",
    openapi_url="/openapi.json",
    urls_namespace="api",
    # auth=AuthBearer(),  # Enable for all endpoints
)

# Register routers
api.add_router("", core_router)  # Health checks at root level
# api.add_router("/auth", auth_router, tags=["Authentication"])
# api.add_router("/users", users_router, tags=["Users"])


# Add exception handlers
@api.exception_handler(ValueError)
def value_error_handler(request, exc):
    return api.create_response(request, {"error": str(exc)}, status=400)


@api.exception_handler(PermissionError)
def permission_error_handler(request, exc):  # noqa: ARG001
    return api.create_response(
        request,
        {"error": "You don't have permission to perform this action"},
        status=403,
    )

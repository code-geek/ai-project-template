"""Main API configuration for Django Ninja."""

from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI
from ninja.security import HttpBearer

from apps.core.api import router as core_router


class AuthBearer(HttpBearer):
    """JWT Bearer token authentication."""

    def authenticate(self, request: HttpRequest, token: str) -> str | None:  # noqa: ARG002
        # TODO(dev): Implement JWT validation
        #            See: https://github.com/project/issues/123
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
)

# Register routers
api.add_router("", core_router)  # Health checks at root level


# Add exception handlers
@api.exception_handler(ValueError)
def value_error_handler(request: HttpRequest, exc: ValueError) -> HttpResponse:
    return api.create_response(request, {"error": str(exc)}, status=400)


@api.exception_handler(PermissionError)
def permission_error_handler(
    request: HttpRequest,
    exc: PermissionError,  # noqa: ARG001
) -> HttpResponse:
    return api.create_response(
        request,
        {"error": "You don't have permission to perform this action"},
        status=403,
    )

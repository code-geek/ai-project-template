from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI

from apps.core.api import router as core_router
from apps.users.api import router as users_router

api = NinjaAPI(
    title="Project API",
    version="1.0.0",
    description="API for Project",
    docs_url="/docs",
)

# Register routers
api.add_router("/users/", users_router, tags=["users"])
api.add_router("/core/", core_router, tags=["core"])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
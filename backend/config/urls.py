"""URL configuration for the project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path

from config.api_config import api

urlpatterns: list[URLPattern | URLResolver] = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

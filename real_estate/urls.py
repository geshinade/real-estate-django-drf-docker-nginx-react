from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version="v1",
        description="API endpoints for the Real Estate API course",
        contact=openapi.Contact(email="geshinaderemi06@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
	path("api/v1/auth/", include("djoser.urls.jwt")),
]

admin.site.site_header = "Real Estate API Admin"
admin.site.site_title = "Real Estate API Admin Portal"
admin.site.index_title = "Welcome to the Real Estate API Portal"

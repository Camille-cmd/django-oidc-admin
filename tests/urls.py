from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("mozilla_django_oidc.urls")),
    path("admin/", admin.site.urls),
]

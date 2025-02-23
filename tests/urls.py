from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("django_oidc_admin.urls")),
    path("admin/", admin.site.urls),
]

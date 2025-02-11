from django.urls import path, include

urlpatterns = [
    path("", include("mozilla_django_oidc.urls")),
]

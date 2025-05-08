"""
URL configuration for simple_blog project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("accounts.urls", namespace="accounts")),
]

from django.contrib import admin
from django.urls import path, include

from .views import health_check


urlpatterns = [
    path('health_check/', health_check.health_check),
]

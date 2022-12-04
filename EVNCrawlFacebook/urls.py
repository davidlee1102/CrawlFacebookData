from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('health_check/', include('health_check.urls')),
]

from django.contrib import admin
from django.urls import path, include

from .views import health_check, facebook_data_crawl_request

urlpatterns = [
    path('health_check/', health_check.health_check),
    path('comment_check/', facebook_data_crawl_request.get_comment)
]

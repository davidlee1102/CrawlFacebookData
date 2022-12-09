from django.urls import path

from .views import health_check, facebook_data_crawl_request
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('comment_check/', facebook_data_crawl_request.get_comment),
    path('', health_check.health_check),
]


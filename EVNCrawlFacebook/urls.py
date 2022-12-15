from django.urls import path

from .views import health_check, facebook_data_crawl_request, file_request
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('comment_check/', facebook_data_crawl_request.get_comment),
    path('general_info_check/', facebook_data_crawl_request.get_general_information),
    path('', health_check.health_check),
    # path('comment_check/download_file/', file_request.download_file),
]

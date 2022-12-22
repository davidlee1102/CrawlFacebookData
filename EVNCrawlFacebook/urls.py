from django.urls import path

from .views import health_check, facebook_data_crawl_request, file_request

urlpatterns = [
    path('comment_check/', facebook_data_crawl_request.get_comment),
    path('general_info_check/', facebook_data_crawl_request.get_general_information),
    path('specific_info_check/', facebook_data_crawl_request.get_specific_information),
    path('', health_check.health_check),
    path('health_check/', health_check.health_check),
    path('download_file/', file_request.download_file),

]

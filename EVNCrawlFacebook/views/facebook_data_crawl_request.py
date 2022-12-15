import time

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from EVNCrawlFacebook.utils import get_comments, file_process, response_message_process


@api_view(["POST"])
def get_comment(request: Request):
    """Example
    {
        "link_post": "https://mbasic.facebook.com/groups/www.happynest.vn/posts/1366498990858866/",
        "number_comment": 5
    }
    """
    data = request.data
    link_request = data.get("link_post", "")
    number_comment = data.get("number_comment", "")
    if not number_comment:
        number_comment = 0

    if not link_request or not isinstance(number_comment, int):
        return Response(response_message_process.status_response('error input'), status=status.HTTP_400_BAD_REQUEST)
    else:
        comments_list = get_comments.process_comment(link_request, number_comment)
        if not comments_list:
            return Response(response_message_process.status_response('error input'), status=status.HTTP_400_BAD_REQUEST)
        else:
            file_creation_check = file_process.convert_list_to_json(comments_list)
            if file_creation_check:
                return Response(comments_list, status=status.HTTP_200_OK)
            else:
                return Response(comments_list, status=status.HTTP_200_OK)

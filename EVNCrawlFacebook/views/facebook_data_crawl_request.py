from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from EVNCrawlFacebook.utils import get_comments


@api_view(["POST"])
def get_comment(request: Request):
    """Example
    {
        "link_post": "https://www.facebook.com/groups/630943070407078/subgroups/1331640773991372/posts/1444534716035310/",
        "number_comment": 5
    }
    """
    data = request.data
    link_request = data.get("link_post", "")
    number_comment = data.get("number_comment", "")
    if not number_comment:
        number_comment = 0

    messsage = {
        'message': 'error input'
    }
    if not link_request or not isinstance(number_comment, int):
        return Response(messsage, status=status.HTTP_400_BAD_REQUEST)
    else:
        comments_list = get_comments.process_comment(link_request, number_comment)
        if not comments_list:
            return Response(messsage, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(comments_list, status=status.HTTP_200_OK)

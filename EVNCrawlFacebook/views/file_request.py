import os
from django.http import HttpResponse, Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(["GET"])
def download_file(request):
    file_path = "EVNCrawlFacebook/data_save/evn_comment_list.csv"
    if request.method == 'GET':
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404
    else:
        raise Http404

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class GetSiteHTMLAPIView(APIView):
    def get_html(self, url):
        response = requests.get(url)
        html_code = response.text
        return html_code

    def get(self, request):
        url = request.query_params.get('url')

        if not url:
            return Response({'error': 'URL parameter is required'}, status=400)

        html_code = self.get_html(url)

        return Response({'html_code': html_code})
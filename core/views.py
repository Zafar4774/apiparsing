from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup


class InstagramParser(APIView):
    def post(self, request, *args, **kwargs):
        user_url = request.data.get('url')
        if not user_url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.get(user_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            return Response({"html": str(soup)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

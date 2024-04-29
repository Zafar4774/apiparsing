from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class GetInstagramData(APIView):
    def get(self, request):
        url = 'https://www.instagram.com/'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return Response({"response": response.text})
            else:
                return Response({"error": "Ошибка при выполнении запроса. Код состояния: {}".format(response.status_code)})
        except requests.exceptions.RequestException as e:
            return Response({"error": "Произошла ошибка при выполнении запроса: {}".format(e)})
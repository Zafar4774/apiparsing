from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


def get_tags(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = [tag.name for tag in soup.find_all()]
        return JsonResponse({'tags': tags})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

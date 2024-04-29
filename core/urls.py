from django.urls import path
from .views import InstagramParser

urlpatterns = [
    path('parse_page/', InstagramParser.as_view(), name='parse_page'),
]
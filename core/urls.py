from django.urls import path
from .views import get_tags

urlpatterns = [
    path('get_tags/', get_tags, name='get_tags'),
]
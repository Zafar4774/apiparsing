from django.urls import path
from .views import GetInstagramData

urlpatterns = [
    path('get_tags/', GetInstagramData.as_view(), name='get_tags'),
]
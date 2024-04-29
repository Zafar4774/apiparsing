from django.urls import path
from .views import GetSiteHTMLAPIView

urlpatterns = [
    path('get_tags/', GetSiteHTMLAPIView.as_view(), name='get_tags'),
]
from django.urls import path
from .views import CrawlerAPIList


urlpatterns = [
    path('list/', CrawlerAPIList.as_view(), name="crawler_list")
]

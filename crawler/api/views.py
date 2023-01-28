from django.shortcuts import render

from rest_framework.generics import ListAPIView

from crawler.models import Crawler, Attribute

from .serializers import CrawlerSerializer 

# Create your views here.
class CrawlerAPIList(ListAPIView):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer
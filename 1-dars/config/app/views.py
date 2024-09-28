from django.shortcuts import render
from .models import News
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import NewsSerializer
# Create your views here.

class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
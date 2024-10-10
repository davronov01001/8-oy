from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

class ListAPINews(APIView):
    def get(self, request:Request):
         
        news = News.objects.all()
        
        return Response(NewsSerializer(news, many=True).data)
    
    def post(self, request:Request):
        print()
        print(request.data)
        print()
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            news = News.objects.create(
                title = request.data["title"],
                content = request.data["content"],
                author = request.data["author"]
            )
            
        return Response("test")

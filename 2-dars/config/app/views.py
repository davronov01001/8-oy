from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import *


# Create your views here.

class ListAPINews(APIView):
    def get(self, request:Request):
         
        news = News.objects.all()
        
        return Response({"news" : news})
    
    # def post(self, request:Request):
    #     return Response()
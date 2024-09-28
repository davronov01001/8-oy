from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import News
from .serialziers import NewsSerializer


class ListAPINews(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                news = News.objects.get(pk=pk)
                return Response(NewsSerializer(news).data)
            except:
                return Response({'message': 'does not exist'})
        news = News.objects.all()
        return Response(NewsSerializer(news, many=True).data)
    def post(self, request: Request, pk = None):
        if not pk:    
            serializer = NewsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            news = serializer.save()
            return Response(NewsSerializer(news).data)
        return Response({'message':'Method not allowed'})
    def put(self, request: Request, pk):
        if pk:
            try:
                news = News.objects.get(pk=pk)
                serializer = NewsSerializer(instance=news, data=request.data)
                serializer.is_valid(raise_exception=True)
                news = serializer.save()
                return Response(NewsSerializer(news).data)
            except:
                return Response({'message': 'does not exist'})
        return Response({'message':'Method PUT not allowed  '})
    def delete(self, request: Request, pk=None):
        if pk:    
            news = News.objects.get(pk=pk)
            news.delete()
            return Response({'status':'success'})
        else: 
            return Response({'status':'fail'})
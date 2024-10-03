from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from .models import *
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.

class CarViewSet(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request:Request, pk=None):
        if pk:
            queryset = Car.objects.get(pk=pk)
            serializer = CarSerializer(queryset)
            return Response(serializer.data)
        return Response({"error": "404"})    

    def create(self, request:Request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def update(self, request:Request, pk=None):
        if pk:
            queryset = Car.objects.get(pk=pk)
            serializer = CarSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({"error": "404"})
    
    def destroy(self, request:Request, pk=None):
        if pk:
            queryset = Car.objects.get(pk=pk)
            queryset.delete()
            return Response({"message": "Car deleted"})
        return Response({"error": "404"})
    



    
class BrandView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BrandDetail(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]
    

class ColorView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ColorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAdminUser]



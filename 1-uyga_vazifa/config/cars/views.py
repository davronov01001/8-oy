from django.shortcuts import render
from .models import Car, CarBrand
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CarSerializer
# Create your views here.

class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
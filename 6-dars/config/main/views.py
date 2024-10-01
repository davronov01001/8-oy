from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView  
# Create your views here.
class Car(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
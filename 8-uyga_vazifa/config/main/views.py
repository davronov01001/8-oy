from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class ClubView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
    
class AthleteView(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

class SportView(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]

class SportTypeView(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
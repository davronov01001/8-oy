from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.permissions import DjangoModelPermissions

from .models import *
from .serializers import *
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]

class SalesManView(viewsets.ModelViewSet):
    queryset = SalesMan.objects.all()
    serializer_class = SalesManSerializer
    permission_classes = [DjangoModelPermissions]


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [DjangoModelPermissions]

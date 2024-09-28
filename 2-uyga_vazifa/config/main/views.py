from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Books, Watches, Clothes
from .serializers import BooksSerializer, ClothesSerializer, WatchesSerializer

class BookList(APIView):
    def get(self, request:Request):
        books = Books.objects.all()
        book = BooksSerializer(books, many=True)
        return Response(book.data)
class WatchesList(APIView):
    def get(self, request:Request):
        watches = Watches.objects.all()
        return Response({'watches': watches})
class ClothesList(APIView):
    def get(self, request:Request):
        clothes = Clothes.objects.all()
        return Response({'clothes': clothes})
    

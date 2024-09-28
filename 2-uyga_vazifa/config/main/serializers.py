from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
import io

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

book = Book(title="Dark Psychology", author="Machiavil", publication_year=2024)

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    publication_year = serializers.IntegerField()

def book_to_json():
    serializer = BookSerializer(book)
    print(serializer.data)
    print()
    print("-----")
    print()
    json = JSONRenderer().render(serializer.data)
    print(json)

def json_to_python():
    json = b'{"title":"Dark Psychology","author":"Machiavil","publication_year":2024}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = BookSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data) 


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class ClothesSerializer(ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'


class WatchesSerializer(ModelSerializer):
    class Meta:
        model = Watches
        fields = '__all__'
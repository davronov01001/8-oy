from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import MovieSerializer
# Create your views here.
class ListView(APIView):
    def get(self, request:Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(movie)
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"error": "Movie not found"})
            
        movies = Movie.objects.all()
        return Response(MovieSerializer(movies, many=True).data)
    
    def post(self, request:Request, pk=None):
        if not pk:    
            serializer = MovieSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movies = serializer.save()
            return Response(MovieSerializer(movies).data)
        return Response({'message':'Method POST not allowed'})

    def put(self, request:Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(instance=movie, data=request.data)
                serializer.is_valid(raise_exception=True)
                movie = serializer.save()
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"error": "movie not found"})
        return Response({'message':'Method PUT not allowed'})

    def delete(self, request:Request, pk=None):
        if pk:
            try:
                movie = Movie.objects.get(pk=pk)
                movie.delete()
                return Response({"message": "movie deleted successfully"})
            except:
                return Response({"error": "movie not found"})
        return Response({'message':'Method DELETE not allowed'})
from django.urls import path
from .views import *

urlpatterns = [
    path('Genre', GenreAPIView.as_view() ), 
    path('Book', BookAPIView.as_view() ),
    path('Author', AuthorAPIView.as_view() ),
    path('Author/<int:pk>', AuthorDetailAPIView.as_view() ),
    path('Book/<int:pk>', BookDetailAPIView.as_view() ),
    path('Genre/<int:pk>', GenreDetailAPIView.as_view() )
]
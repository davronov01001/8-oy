from django.contrib import admin
from django.urls import path

from .views import ListAPINews

urlpatterns = [
    path('', ListAPINews.as_view()),
    path('<int:pk>/', ListAPINews.as_view()),
]

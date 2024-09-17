from django.urls import path
from .views import CarAPIView, CarDetailAPIView

urlpatterns = [
    path('api/cars/', CarAPIView.as_view()),
    path('api/cars/<int:pk>/', CarDetailAPIView.as_view()),
]
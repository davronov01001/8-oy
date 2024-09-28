from django.urls import path 
from .views import *

urlpatterns = [
    path('api/v1', NewsAPIView.as_view()),
    path('api/v1/<int:pk>/', NewsDetailAPIView.as_view()),
    
]
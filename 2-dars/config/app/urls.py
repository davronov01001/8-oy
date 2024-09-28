from django.urls import path
from .views import ListAPINews

urlpatterns = [
    path('', ListAPINews.as_view())
]
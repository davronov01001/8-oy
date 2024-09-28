from django.urls import path
from .views import ListView
urlpatterns = [
    path('', ListView.as_view()),
    path('<int:pk>/', ListView.as_view()),
]
from django.urls import path
from .views import BookList
urlpatterns = [
    path('v1', BookList.as_view())
]
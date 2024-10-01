from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CarView.as_view()),
    path('car/<int:pk>', CarDetail.as_view()),
    path('brand/', BrandView.as_view()),
    path('brand/<int:pk>', BrandDetail.as_view()),
    path('color/', ColorView.as_view()),
    path('color/<int:pk>', ColorDetail.as_view()),
]
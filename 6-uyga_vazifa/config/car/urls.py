from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CarViewSet.as_view({"get": "list", "post": "create"})),
    path('car/<int:pk>', CarViewSet.as_view({"get":"retrieve", "put":"update", "delete": "destroy"})),
    path('brand/', BrandView.as_view()),
    path('brand/<int:pk>', BrandDetail.as_view()),
    path('color/', ColorView.as_view()),
    path('color/<int:pk>', ColorDetail.as_view()),
]
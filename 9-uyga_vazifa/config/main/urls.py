from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', ProductView)
router.register('tags', TagView)
router.register('categories', CategoryView)
router.register('salesmen', SalesManView)

urlpatterns = router.urls
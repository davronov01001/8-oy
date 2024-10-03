from .views import *
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register('receipts', ReceiptViewSet, basename='receipt' )
router.register('foods', FoodViewSet, basename='food' )
router.register('categories', CategoryViewSet, basename='category' )
urlpatterns = router.urls
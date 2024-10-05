from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('clubs', ClubView, basename='club')
router.register('athlets', AthleteView, basename='athlete')
router.register('sports', SportView, basename='sport')
router.register('sport-types', SportTypeView, basename='sport-type')

urlpatterns = router.urls
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movie', MovieViewset)
router.register(r'theatre', TheatreViewset)
router.register(r'screen', ScreenViewset)
router.register(r'showtime', ShowDetailViewset)

urlpatterns = [
    path('', include(router.urls)),
]



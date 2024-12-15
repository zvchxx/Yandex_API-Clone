from django.urls import path, include

from rest_framework.routers import DefaultRouter
    
from restaurant.views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')

urlpatterns = [
    path('', include(router.urls)),
]
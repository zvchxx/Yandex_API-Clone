from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurants')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'orders', views.OrderViewSet, basename='orders')


urlpatterns = [
    path('/', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
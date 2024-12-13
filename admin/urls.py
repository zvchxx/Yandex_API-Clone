from django.urls import path, include

from rest_framework.routers import DefaultRouter

from admin import views

router = DefaultRouter()
router.register(r'restaurants', views.ManagerViewSet)
router.register(r'products', views.CourierViewSet)


urlpatterns = [
    path('/', include(router.urls)),
]
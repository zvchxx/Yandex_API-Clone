from django.urls import path, include

from rest_framework.routers import DefaultRouter

from admin import views

router = DefaultRouter()
router.register(r'managaer', views.ManagerViewSet, basename='manager')
router.register(r'courtier', views.CourierViewSet, basename='courier')


urlpatterns = [
    path('', include(router.urls)),
]
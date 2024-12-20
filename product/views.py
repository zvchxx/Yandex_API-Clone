from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from product import models
from product import serializers
from product.paginations import CustomPagination
from product.permissions import IsManager


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = models.RestaurantModel.objects.all()
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsManager]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsManager()]
        return super().get_permissions()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsManager]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'restaurant'] 

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsManager()]
        return super().get_permissions()
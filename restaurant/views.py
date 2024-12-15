from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from restaurant.permissions import IsManager
from restaurant.models import RestaurantModel
from restaurant.serializers import RestaurantSerializer
from restaurant.paginations import CustomPagination

class RestaurantViewSet(ModelViewSet):
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsManager]
    pagination_class = CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from order.permissions import IsManager
from order.paginations import CustomPagination
from order.models import OrderModel
from order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()  
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated, IsManager]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
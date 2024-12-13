from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from user.models import UserModel

from admin.serializers import ManagerSerializer, CourierSerializer


class ManagerViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAdminUser]


class CourierViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsAdminUser]
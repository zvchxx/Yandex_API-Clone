from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from branch.permissions import IsManager
from branch.models import BranchModel
from branch.serializers import BranchSerializer
from branch.paginations import CustomPagination

class BranchViewSet(ModelViewSet):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated, IsManager]
    pagination_class = CustomPagination

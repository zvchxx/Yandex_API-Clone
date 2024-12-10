from rest_framework import viewsets, permissions

from feedback.models import FeedbackModel
from feedback.serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self): 
        user = self.request.user
        if user.is_staff:
            return FeedbackModel.objects.all()
        return FeedbackModel.objects.filter(user=user)
from rest_framework import serializers

from feedback.models import FeedbackModel

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username") 

    class Meta:
        model = FeedbackModel
        fields = [
            "id",
            "user",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
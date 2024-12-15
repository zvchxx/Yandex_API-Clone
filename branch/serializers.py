from branch import models

from rest_framework import serializers

from user.serializers import UserSerializer

class BranchSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)

    class Meta:
        model = models.BranchModel
        fields = ['id', 'name', 'address', 'manager', 'restaurant']
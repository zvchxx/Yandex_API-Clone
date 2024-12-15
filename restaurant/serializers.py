from restaurant import models

from rest_framework import serializers

from user.serializers import UserSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = models.RestaurantModel
        fields = ['id', 'name', 'address', 'phone_number', 'owner', 'image']
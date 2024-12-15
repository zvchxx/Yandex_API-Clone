from product import models

from rest_framework import serializers

from restaurant.serializers import RestaurantSerializer

from user.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = models.ProductModel
        fields = ['id', 'restaurant', 'name', 'description', 'price', 'stock', 'image']
        extra_kwargs = {
            'restaurant': {'required': False},
        }
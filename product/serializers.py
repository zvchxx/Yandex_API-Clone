from product import models

from rest_framework import serializers

from user.serializers import UserSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = models.RestaurantModel
        fields = ['id', 'name', 'address', 'phone_number', 'owner']


class ProductSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = models.ProductModel
        fields = ['id', 'restaurant', 'name', 'description', 'price', 'stock', 'image']
        extra_kwargs = {
            'restaurant': {'required': False},
        }


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProductModel
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = models.OrderModel
        fields = ['id', 'customer', 'restaurant', 'products', 'total_price', 'delivery_address', 'status', 'created_at']
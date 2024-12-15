from rest_framework import serializers

from order.models import OrderModel, OrderProductModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['id', 'customer', 'courier', 'status', 'order_items']

    def create(self, validated_data):
        basket = validated_data.pop('basket')
        order = OrderModel.objects.create(**validated_data)
        
        for item in basket.items.all():
            item_data = {
                'quantity': item.quantity,
                'total_price': item.product.price * item.quantity,
            }
            order_item = OrderProductModel.objects.create(order=order, **item_data)
            order.items.add(order_item)
            basket.items.remove(item)
            basket.save()

        order.save()
        return order

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate(self, attrs):
        basket = attrs.get('basket')
        if not basket or not basket.items.all():
            raise serializers.ValidationError('Basket must not be empty.')
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('is_deleted', None)

        data['restaurant'] = {
            "id": instance.restaurant.id,
            "name": instance.restaurant.name
        }
        data['branch'] = {
            "id": instance.branch.id,
            "unique_name": instance.branch.name,
            "phone_number": instance.branch.user.phone_number,
            "address": instance.branch.address
        }
        
        data['user'] = {
            "id": instance.user.id,
            "first_name": instance.user.first_name,
            "phone_number": instance.user.phone_number
        }
        data['courier'] = {
            "id": instance.courier.id,
            "unique_name": instance.courier.courier.name,
            "first_name": instance.courier.first_name,
            "phone_number": instance.courier.phone_number
        }

        data['delivery_address'] = {
            "id": instance.delivery_address.id,
            "address": instance.delivery_address.address
        }
        
        data['order_items'] = [
            {
                'product_id': item.product.id,
                'product_name': item.product.name,
                'product_category_id': item.product.category.id,
                'product_category_name': item.product.category.name,
                'quantity': item.quantity,
                'price_per_item': item.price_per_item,
                'total_price': item.total_price
            } for item in instance.items.all()
        ]
        
        data['total_items'] = instance.total_items
        data['total_price'] = instance.total_price
        return data
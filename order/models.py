from django.db import models

from branch.models import BranchModel

from product.models import ProductModel

from user.models import UserModel

from restaurant.models import RestaurantModel


class OrderProductModel(models.Model):
    order = models.ForeignKey('OrderModel', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('completed-restaurant', 'Completed--restaurant'),
        ('delivering', 'Delivering'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE, limit_choices_to={'user_type': 'customer'})
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE)  
    products = models.ManyToManyField(ProductModel, through='OrderProductModel')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress') 
    courier = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name='my_delivering',
        verbose_name='Courier',
        null=True,
        limit_choices_to={'user_type': 'courier'}
    )
    order_items = models.ManyToManyField(
        'OrderProductModel',
        related_name='orders',
        verbose_name='Order Items'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

    class Meta:
        ordering = ['-id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def total_items(self):
        return sum(item.quantity for item in self.order_items.all())

    @property
    def total_price(self):
        return sum(item.total_price for item in self.order_items.all())
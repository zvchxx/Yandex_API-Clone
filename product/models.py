from django.db import models

from user.models import UserModel

from restaurant.models import RestaurantModel

class ProductModel(models.Model):
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE, limit_choices_to={'user_type': 'customer'})
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, through='OrderProductModel')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    
class OrderProductModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'


class PaymentModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    paid_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.status}"
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
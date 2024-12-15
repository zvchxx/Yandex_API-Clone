from django.db import models
from django.contrib.auth import get_user_model

from product.models import ProductModel

User = get_user_model()


class BasketItemModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name="basket_items",
        verbose_name="Product"
    )
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"


class BasketModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="baskets",
        verbose_name="User"
    )
    items = models.ManyToManyField(
        BasketItemModel,
        related_name="baskets",
        verbose_name="Basket Items"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Basket #{self.pk} | User: {self.user.email}"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"
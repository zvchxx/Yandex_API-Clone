from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CourierModel(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name", unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courier",
        verbose_name="User",
        limit_choices_to={'user_type': 'courier'}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Courier"
        verbose_name_plural = "Couriers"

    def __str__(self):
        return self.name
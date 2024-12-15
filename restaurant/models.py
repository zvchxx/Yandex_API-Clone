from django.db import models

from user.models import UserModel


class RestaurantModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='restaurant/', null=True, blank=True)
    owner = models.ForeignKey(UserModel, on_delete=models.SET_NULL,
    null=True, blank=True, limit_choices_to={'user_type': 'restaurant'})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
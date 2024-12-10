from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.username
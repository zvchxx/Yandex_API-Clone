from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('restaurant', 'Restaurant'),
        ('admin', 'Admin'),
        ('branch', 'Branch'),   
    )

    USER_STATUS = (
        ('active', 'Active'),
        ('delete', 'Delete'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')
    user_status = models.CharField(max_length=10, choices=USER_STATUS, default='active')
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.username
    
class UserLocations(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name='User'
    )
    address = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'User Location'
        verbose_name_plural = 'User Locations'
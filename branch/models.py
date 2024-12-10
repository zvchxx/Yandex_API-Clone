from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from restaurant.models import RestaurantModel


User = get_user_model()


class BranchModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("Name"), unique=True)
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Phone Number"))
    longitude = models.FloatField()
    latitude = models.FloatField()
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="branches",
        verbose_name=_("Manager")
    )
    restaurant = models.ForeignKey(
        RestaurantModel,
        on_delete=models.CASCADE,
        related_name="branches",
        verbose_name=_("Restaurant")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")
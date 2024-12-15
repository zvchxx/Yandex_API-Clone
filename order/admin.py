from django.contrib import admin

from order import models

admin.site.register(models.OrderModel)
admin.site.register(models.OrderProductModel)
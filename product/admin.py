from django.contrib import admin

from product import models

admin.site.register(models.ProductModel)
admin.site.register(models.RestaurantModel)
admin.site.register(models.OrderModel)
admin.site.register(models.OrderProductModel)
admin.site.register(models.PaymentModel)
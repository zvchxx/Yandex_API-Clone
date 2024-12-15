from django.contrib import admin

from basket.models import BasketItemModel, BasketModel


admin.site.register(BasketItemModel)
admin.site.register(BasketModel)
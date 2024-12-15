from django.contrib import admin

from product import models

admin.site.register(models.ProductModel)
admin.site.register(models.CategoryModel)
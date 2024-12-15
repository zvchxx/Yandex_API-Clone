from django.db import models

from restaurant.models import RestaurantModel

from branch.models import BranchModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="products"
    )
    branch = models.ForeignKey(
        BranchModel,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=("Branch")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
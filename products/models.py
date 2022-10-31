from django.db import models


class CategoryModel(models.Model):
    """
    Category Model
    """
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    """
    Product Model
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField(max_length=2, null=True)
    created_at = models.DateTimeField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True)
    brand = models.CharField(max_length=100, blank=True)
    quality = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)

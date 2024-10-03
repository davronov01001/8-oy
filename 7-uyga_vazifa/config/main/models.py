from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingridients = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
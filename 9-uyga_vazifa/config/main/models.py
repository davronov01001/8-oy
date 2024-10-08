from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SalesMan(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.ManyToManyField(Tag)
    description = models.TextField()
    sales_man = models.ForeignKey(SalesMan, on_delete=models.CASCADE)
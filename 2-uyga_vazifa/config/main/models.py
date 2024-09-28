from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100,blank=True)
    short_description = models.TextField(blank=True)
    publication_date = models.DateField(blank=True, null=True)

class Watches(models.Model):
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Clothes(models.Model):
    brand = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
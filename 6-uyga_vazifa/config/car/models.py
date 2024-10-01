from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True)

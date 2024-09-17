from django.db import models

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    ctype = models.CharField(max_length=20)
    year = models.DateField(null=True)


from django.contrib import admin
from .models import CarBrand, Car
# Register your models here.
admin.site.register(Car)
admin.site.register(CarBrand)
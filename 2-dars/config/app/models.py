from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
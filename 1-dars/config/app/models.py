from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title
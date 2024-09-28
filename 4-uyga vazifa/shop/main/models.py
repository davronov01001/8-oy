from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    text = models.TextField()
    def __str__(self) -> str:
        return self.text

class Movie(models.Model):
    name = models.CharField(max_length=100, blank=True)
    quantity_of_actors = models.PositiveIntegerField(blank=True)
    studio = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
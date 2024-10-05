from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Athlete(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class SportType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Sport(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)

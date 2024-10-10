from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Days(models.Model):
    week_day = models.CharField(max_length=15)

    def __str__(self):
        return self.week_day


class Room(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField(default=16, help_text="O'quvchi sig'imi")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


STATUS = [
    ('du', "Du"),
    ('se', "Se"),
    ('chor', "Chor"),
    ('pay', "Pay"),
    ('ju', "Ju"),
    ('shan', "Shan"),
    ('yak', "Yak"),
]


class CourseGroup(models.Model):
    number = models.CharField(max_length=5, help_text="Guruh raqami. M: FN21")
    start_date = models.DateField()
    end_date = models.DateField()
    time_lesson = models.TimeField()
    days = models.ManyToManyField(Days)
    status = models.CharField(max_length=4, choices=STATUS)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return self.number

class Lesson(models.Model):
    course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)
    



class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(CourseGroup)
    experience = models.IntegerField(default=1)
    is_working = models.BooleanField(default=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    courses = models.ManyToManyField(CourseGroup)


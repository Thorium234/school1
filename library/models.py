from django.db import models
from .models import  models
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    publishers=models.CharField(max_length=255)
    first_publication=models.PositiveIntegerField()
    ISBN=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    admision_number=models.PositiveIntegerField()
    stream=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
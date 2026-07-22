from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10)
    place = models.CharField(max_length=10)
    image = models.FileField(upload_to="studentimages")
    
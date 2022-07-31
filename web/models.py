from django.db import models

# Create your models here.
class client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # email = models.EmailField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()
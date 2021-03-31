from django.db import models

# Create your models here.
class Person(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    psw = models.CharField(max_length=30)
    
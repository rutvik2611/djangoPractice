from django.db import models

# Create your models here.
class LOGIN(models.Model):
    name = models.CharField(max_length=40)
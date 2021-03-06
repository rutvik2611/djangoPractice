from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
class Regsistration(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    username = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=40)
    email =models.EmailField(unique = True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    
    def __str__(self):
        return self.username


class BlogRegsistration(models.Model):
    name = models.CharField(max_length = 200)
    value = models.TextField(blank = True)
    
    
    def __str__(self):
        return self.name

#Serializer<- convert model to JSON data


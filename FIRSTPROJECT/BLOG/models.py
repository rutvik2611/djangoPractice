from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class LOGIN(models.Model):
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    username = models.CharField(max_length=40)
    user_password = models.CharField(max_length=40)
    email =models.EmailField()
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
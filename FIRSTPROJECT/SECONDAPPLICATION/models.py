from django.db import models

# Create your models here.
def register(models.Model):
    First_name=models.CharField(max_length=40)
    Last_name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=40)
    Password=models.CharField(max_length=40)
    
    def __str__(self):
        return self.First_name

def register_blog(register):
    BlogName=models.CharField(max_length=40)

     def __str__(self):
        return self.BlogName
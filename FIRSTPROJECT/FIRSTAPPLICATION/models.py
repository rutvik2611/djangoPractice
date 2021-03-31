from django.db import models

# Create your models here.
class Person(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    psw = models.CharField(max_length=30)


class Training(models.Model):
    session = models.CharField(max_length=5,unique=True)
    def __str__(self):
        return self.session

class Students(models.Model):
    name = models.CharField(max_length=30)
    session=models.ForeignKey("Training", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
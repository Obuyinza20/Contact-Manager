from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Contact(models.Model):
    owner=models.CharField(max_length=200, default='anonymous')
    full_name = models.CharField(max_length=200)
    relationship =models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    phone =models.IntegerField()  # we could also asign an integerfield
    address  = models.CharField(max_length=200)


    def __str__(self):
        return self.full_name


# class User(AbstractUser):
#     UserName = models.CharField(max_length=200 , unique=True)
#     Password = models.CharField(max_length=200)
#     ConfirmP = models.CharField(max_length=200)


#     USERNAME_FIELD ='UserName'
#     REQUIRED_FIELDS=[]



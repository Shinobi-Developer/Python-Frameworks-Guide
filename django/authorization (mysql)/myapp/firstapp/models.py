from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'users'      

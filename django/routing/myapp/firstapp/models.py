from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'users'
from django.contrib.auth.models import User
from django.db import models

class signup(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    birthdate=models.CharField(max_length=255)
    pwd = models.CharField(max_length=10)
    repwd=models.CharField(max_length=10)
    gender=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    phno=models.CharField(max_length=255,default='')
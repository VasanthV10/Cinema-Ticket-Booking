from django.contrib.auth.models import User
from django.db import models

class signuptheatre(models.Model):
    email = models.CharField(max_length=255)
    tname=models.CharField(max_length=255)
    pwd = models.CharField(max_length=10)
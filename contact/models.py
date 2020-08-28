from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class contactform(models.Model):
    tname = models.CharField(max_length=200,default='')
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    content = models.CharField(max_length=2000)

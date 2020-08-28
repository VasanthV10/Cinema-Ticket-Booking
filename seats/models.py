from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class seat(models.Model):
    seats=models.CharField(max_length=255,null=True)

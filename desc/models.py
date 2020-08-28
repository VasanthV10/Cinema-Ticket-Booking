from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class actorpic(models.Model):
    aname = models.CharField(max_length=200)
    apic=models.CharField(max_length=2000)

class actresspic(models.Model):
    asname = models.CharField(max_length=200)
    aspic=models.CharField(max_length=2000)
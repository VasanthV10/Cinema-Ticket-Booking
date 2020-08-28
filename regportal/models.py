from django.contrib.auth.models import User
from django.db import models
class moviereg(models.Model):
    theatrename = models.CharField(max_length=30)
    moviename = models.CharField(max_length=255)
    actor=models.CharField(max_length=255)
    actress = models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    poster=models.CharField(max_length=255)
    stime=models.TextField()
    subject=models.TextField()
    rowss=models.BigIntegerField()
    colss=models.BigIntegerField()
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    trailer=models.CharField(max_length=255)
    tpic=models.CharField(max_length=255)
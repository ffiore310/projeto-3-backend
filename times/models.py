# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Time(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    
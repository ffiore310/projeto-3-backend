# Create your models here.
from django.db import models


class Time(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
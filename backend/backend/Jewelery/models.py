from django.db import models


# Create your models here.
class Jewelery(models.Model):
    name = models.CharField()
    price = models.IntegerField()

from django.db import models


# Create your models here.
class Jewelery(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()

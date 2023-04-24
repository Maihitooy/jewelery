from django.db import models

# Create your models here.
from django.utils import timezone


class Jewelery(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(verbose_name='image', blank=False, null=False)  # black=False - не может быть пустым
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default=1, blank=True)
    description = models.TextField(max_length=350, blank=True)
    precious_metal = models.ForeignKey("PreciousMetal", on_delete=models.CASCADE, default=1, blank=True)
    precious_metal_sample = models.ForeignKey("PreciousMetalSample", on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return f'{self.pk}, {self.name}'  # return f'{self.name}, {self.price}' - чтобы вернуть несколько значений


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='image', blank=True, null=True)

    def __str__(self):
        return f'{self.pk}, {self.name}'


class PreciousMetal(models.Model):
    name_metal = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk}, {self.name_metal}'


class PreciousMetalSample(models.Model):
    sample = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pk}, {self.sample}'

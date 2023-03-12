from django.db import models


# Create your models here.
class Jewelery(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    image = models.ImageField(verbose_name='image', blank=False, null=False)  # black=False - не может быть пустым

    def __str__(self):
        return f'{self.pk}, {self.name}'  # return f'{self.name}, {self.price}' - чтобы вернуть несколько значений

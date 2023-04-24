from django.db import models

# Create your models here.
from django.utils import timezone


class Jewelery(models.Model):
    """
    Класс для представления карточки товара.

    Атрибуты
    ------
    name : CharField
        наименование товара
    price : PositiveIntegerField
        цена товара
    image : ImageField
        фотография товара
    category : ForeignKey
        категория, к которой относится товар
    description : TextField
        описание товара
    precious_metal : ForeignKey
        название металла: серебро/золото
    precious_metal_sample : ForeignKey
        проба металла

    Методы
    ------
    __str__():
        Возвращает наименование товара и PrimaryKey.

    """
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(verbose_name='image', blank=False, null=False)  # black=False - не может быть пустым
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default=1, blank=True)
    description = models.TextField(max_length=350, blank=True)
    precious_metal = models.ForeignKey("PreciousMetal", on_delete=models.CASCADE, default=1, blank=True)
    precious_metal_sample = models.ForeignKey("PreciousMetalSample", on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        """
        Возвращает PrimaryKey и наименование товара.
        """
        return f'{self.pk}, {self.name}'  # return f'{self.name}, {self.price}' - чтобы вернуть несколько значений


class Category(models.Model):
    """
        Класс для представления категории товаров.

        Атрибуты
        ------
        name : CharField
            наименование категории
        image : ImageField
            фотография товара

        Методы
        ------
        __str__():
            Возвращает наименование категории и PrimaryKey.

        """
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='image', blank=True, null=True)

    def __str__(self):
        """
        Возвращает PrimaryKey и наименование категории.
        """
        return f'{self.pk}, {self.name}'


class PreciousMetal(models.Model):
    """
        Класс для представления металла.

        Атрибуты
        --------
        name_metal : CharField
            наименование металла

        Методы
        ------
        __str__():
            Возвращает наименование металла и PrimaryKey.

        """
    name_metal = models.CharField(max_length=255)

    def __str__(self):
        """
        Возвращает PrimaryKey и наименование металла.
        """
        return f'{self.pk}, {self.name_metal}'


class PreciousMetalSample(models.Model):
    """
            Класс для представления проб металла.

            Атрибуты
            --------
            sample : PositiveIntegerField
                проба металла

            Методы
            ------
            __str__():
                Возвращает пробу металла и PrimaryKey.

            """
    sample = models.PositiveIntegerField()

    def __str__(self):
        """
        Возвращает PrimaryKey и пробу металла.
        """
        return f'{self.pk}, {self.sample}'

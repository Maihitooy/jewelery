# Serializer в Django - это инструмент, который позволяет преобразовывать
# данные из моделей Django в форматы, которые могут быть переданы через
# API или сохранены в базе данных. Он также может выполнять обратное преобразование,
# то есть преобразование данных из формата API обратно в модели Django.
# Serializer является важным компонентом в построении веб-приложений на Django,
# особенно при работе с RESTful API.

from rest_framework.serializers import ModelSerializer

from Jewelery.models import Jewelery, Category, PreciousMetal, PreciousMetalSample


class CategorySerializer(ModelSerializer):
    """
    Класс сериализует (преобразовывает объекты в типы данных, понятные javascript и front-end фреймворкам) данные для класса Category.
    """
    class Meta:
        """
        Класс Meta определяет метаданные модели Category.

        Атрибуты
        --------
        model :
            модель, к которой относятся метаданные
        fields:
            список полей, которые будут использоваться при сериализации экземпляров модели
        """
        model = Category
        fields = ('id', 'name', 'image')


class PreciousMetalSerializer(ModelSerializer):
    """
    Класс сериализует (преобразовывает объекты в типы данных, понятные javascript и front-end фреймворкам) данные для класса PreciousMetal.
    """
    class Meta:
        """
        Класс Meta определяет метаданные модели PreciousMetal.

        Атрибуты
        --------
        model :
            модель, к которой относятся метаданные
        fields:
            список полей, которые будут использоваться при сериализации экземпляров модели
        """
        model = PreciousMetal
        fields = ('id', 'name_metal')


class PreciousMetalSampleSerializer(ModelSerializer):
    """
    Класс сериализует (преобразовывает объекты в типы данных, понятные javascript и front-end фреймворкам) данные для класса PreciousMetalSample.
    """
    class Meta:
        """
        Класс Meta определяет метаданные модели PreciousMetalSample.

        Атрибуты
        --------
        model :
            модель, к которой относятся метаданные
        fields:
            список полей, которые будут использоваться при сериализации экземпляров модели
        """
        model = PreciousMetalSample
        fields = ('id', 'sample')


class JewelerySerializer(ModelSerializer):
    """
    Класс сериализует (преобразовывает объекты в типы данных, понятные javascript и front-end фреймворкам) данные для класса Jewelery.


    Атрибуты
    --------
    category : CategorySerializer
        категория
    precious_metal : PreciousMetalSerializer
        металл
    precious_metal_sample : PreciousMetalSampleSerializer
        проба металла
    """

    category = CategorySerializer(read_only=True)
    precious_metal = PreciousMetalSerializer(read_only=True)
    precious_metal_sample = PreciousMetalSampleSerializer(read_only=True)

    class Meta:
        """
        Класс Meta определяет метаданные модели Jewelery.

        Атрибуты
        --------
        model :
            модель, к которой относятся метаданные
        fields:
            список полей, которые будут использоваться при сериализации экземпляров модели
        """
        model = Jewelery
        fields = ('id', 'name', 'price', 'image', 'category', 'description', 'precious_metal', 'precious_metal_sample')



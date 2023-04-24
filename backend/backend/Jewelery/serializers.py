# Serializer в Django - это инструмент, который позволяет преобразовывать
# данные из моделей Django в форматы, которые могут быть переданы через
# API или сохранены в базе данных. Он также может выполнять обратное преобразование,
# то есть преобразование данных из формата API обратно в модели Django.
# Serializer является важным компонентом в построении веб-приложений на Django,
# особенно при работе с RESTful API.

from rest_framework.serializers import ModelSerializer

from Jewelery.models import Jewelery, Category, PreciousMetal, PreciousMetalSample


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class PreciousMetalSerializer(ModelSerializer):
    class Meta:
        model = PreciousMetal
        fields = ('id', 'name_metal')


class PreciousMetalSampleSerializer(ModelSerializer):
    class Meta:
        model = PreciousMetalSample
        fields = ('id', 'sample')


class JewelerySerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    precious_metal = PreciousMetalSerializer(read_only=True)
    precious_metal_sample = PreciousMetalSampleSerializer(read_only=True)

    class Meta:
        model = Jewelery
        fields = ('id', 'name', 'price', 'image', 'category', 'description', 'precious_metal', 'precious_metal_sample')



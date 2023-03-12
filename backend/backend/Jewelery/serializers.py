# Serializer в Django - это инструмент, который позволяет преобразовывать
# данные из моделей Django в форматы, которые могут быть переданы через
# API или сохранены в базе данных. Он также может выполнять обратное преобразование,
# то есть преобразование данных из формата API обратно в модели Django.
# Serializer является важным компонентом в построении веб-приложений на Django,
# особенно при работе с RESTful API.

from rest_framework.serializers import ModelSerializer

from Jewelery.models import Jewelery


class JewelerySerializer(ModelSerializer):
    class Meta:
        model = Jewelery
        fields = ('id', 'name', 'price', 'image')

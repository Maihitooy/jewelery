from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from Jewelery.models import Jewelery
from Jewelery.serializers import JewelerySerializer


class JeweleryCRUD(RetrieveUpdateDestroyAPIView):
    """
    Класс JeweleryCRUD реализует CRUD-операции для модели Jewelery.

    Атрибуты
    --------
    queryset:
        набор объектов модели Jewelery, которые будут использоваться для выполнения операций CRUD
    serializer_class:
        класс сериализатора, который будет использоваться для преобразования экземпляров модели в JSON и обратно
    """
    queryset = Jewelery.objects.all()
    serializer_class = JewelerySerializer


class JeweleryListView(ListAPIView):
    """
    Класс JeweleryListView отображает список объектов модели Jewelery.

    Атрибуты
    --------
    queryset:
        набор объектов модели Jewelery, которые будут использоваться для выполнения операций CRUD
    serializer_class:
        класс сериализатора, который будет использоваться для преобразования экземпляров модели в JSON и обратно
    """
    queryset = Jewelery.objects.all()
    serializer_class = JewelerySerializer


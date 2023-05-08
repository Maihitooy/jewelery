from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from Jewelery.models import Jewelery, Category
from Jewelery.serializers import JewelerySerializer, CategorySerializer


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

    def get_queryset(self):
        queryset = Jewelery.objects.all()
        category_id = self.request.query_params.get('category_id', None)

        if category_id is not None:
            return queryset.filter(category__id=category_id)
        return queryset


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


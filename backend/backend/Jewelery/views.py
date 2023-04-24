from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from Jewelery.models import Jewelery
from Jewelery.serializers import JewelerySerializer


class JeweleryCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Jewelery.objects.all()
    serializer_class = JewelerySerializer


class JeweleryListView(ListAPIView):
    queryset = Jewelery.objects.all()
    serializer_class = JewelerySerializer


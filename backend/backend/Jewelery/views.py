from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from Jewelery.models import Jewelery
from Jewelery.serializers import JewelerySerializer


class JeweleryListView(RetrieveUpdateDestroyAPIView):
    queryset = Jewelery.objects.all()
    serializer_class = JewelerySerializer

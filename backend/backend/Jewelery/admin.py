from django.contrib import admin

# Register your models here.
from Jewelery.models import Jewelery, Category, PreciousMetal, PreciousMetalSample

admin.site.register(Jewelery)
admin.site.register(Category)
admin.site.register(PreciousMetal)
admin.site.register(PreciousMetalSample)

from django.contrib import admin
from .models import Ingredient, Dish, Category, Menu

# Register your models here.
admin.site.register([Ingredient, Dish, Category, Menu])
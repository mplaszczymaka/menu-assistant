from django.contrib import admin
from .models import Ingredient, Dish, Category, Menu, Dish_in_basket

# Register your models here.
admin.site.register([Ingredient, Dish, Category, Menu, Dish_in_basket])
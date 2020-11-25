from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Ingredient, Dish, Category, Menu, Dish_in_basket, Basket])
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Menu, Category, Dish, Dish_in_basket

# Create your views here.
def index(request):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus':menus})

def menu(request, menu_pk, category_pk, dish_pk = 0, quantity = 0):
    if quantity == 1:
        dish = Dish.objects.get(pk=dish_pk)
        if Dish_in_basket.objects.filter(name=dish):
            d = Dish_in_basket.objects.get(name=dish)
            d.quantity += 1
            d.save()   
        else:
            Dish_in_basket.objects.create(name=dish, quantity=1)

    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()

    # set category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    context =  {'menu'      :   menu,
                'categories':categories,
                'category' : selected_category,
                'dishes': dishes,
                }
    return render(request, 'menu/menu.html', context)

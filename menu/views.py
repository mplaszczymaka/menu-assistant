from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Menu, Category

# Create your views here.
def index(request):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus':menus})

def menu(request, menu_pk, category_pk):
    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()

    # set category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    context =  {'menu'      :   menu,
                'categories':categories,
                'category'  : selected_category,
                'dishes': dishes,
                }
    return render(request, 'menu/menu.html', context)

def add_to_basket(request, menu_pk, category_pk, dish_pk):
    

    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()

    # set category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    context =  {'menu'      :   menu,
                'categories':categories,
                'category'  : selected_category,
                'dishes': dishes,
                }
    return render(request, 'menu/menu.html', context)

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Menu, Category, Dish, Dish_in_basket

# Create your views here.
def index(request):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus':menus})

def menu(request, menu_pk, category_pk, dish_pk_or_name = 0, quantity = 0, show_basket=False):
    """ all behavior of menu_view"""
    # set current menu and its categories
    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()
    
    # set current category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    # add to basket either from menu or from basket
    if quantity == 1: # I want to add to basket
        try:
            dish_pk_or_name = int(dish_pk_or_name) # it is dish_pk when we add from menu
            dish = Dish.objects.get(pk=dish_pk_or_name)
            if Dish_in_basket.objects.filter(name=dish): # if is in basket
                d = Dish_in_basket.objects.get(name=dish)
                d.quantity += 1
                d.save()   
            else:   # if not in basket
                Dish_in_basket.objects.create(name=dish, quantity=1)
        except:
            dish = Dish.objects.get(name=dish_pk_or_name) # it is dish_name when we add from basket
            d = Dish_in_basket.objects.get(name=dish)
            d.quantity += 1
            d.save()
    if quantity == 2: # if I want to remove from basket
        dish = Dish.objects.get(name=dish_pk_or_name)
        d = Dish_in_basket.objects.get(name=dish)
        if d.quantity > 0:
            d.quantity -= 1
            d.save()
            

    dishes_in_basket = Dish_in_basket.objects.all()

    # count number of dishes in basket
    count_dishes = []
    for dish in dishes_in_basket:
        count_dishes.append(dish.quantity)
    count_dishes = sum(count_dishes)

    # count number of pieces in basket
    count_pieces = []
    for dish in dishes_in_basket:
        quantity = Dish.objects.get(name=dish).amount
        how_many = dish.quantity
        count_pieces.append(quantity * how_many)
    count_pieces = sum(count_pieces)

    # assume cost of basket
    count_costs = []
    for dish in dishes_in_basket:
        price = Dish.objects.get(name=dish).price
        how_many = dish.quantity
        count_costs.append(price * how_many)
    count_costs = sum(count_costs)

    # count for how many people is food in basket
    count_portion = []
    for dish in dishes_in_basket:
        portion = Dish.objects.get(name=dish).portion_for
        how_many = dish.quantity
        count_portion.append(portion * how_many)
    count_portion = int(round(sum(count_portion)))



    context =  {'menu'        :   menu,
                'categories'  :   categories,
                'category'    :   selected_category,
                'dish_pk_or_name'     :   dish_pk_or_name,
                'dishes'      :   dishes,
                'dishes_in_basket':dishes_in_basket,
                'count_dishes':   count_dishes,
                'count_pieces':   count_pieces,
                'count_costs' :   count_costs,
                'count_portion':  count_portion,
                'show_basket' :   show_basket,
                }
    return render(request, 'menu/menu.html', context)

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
    """ all behavior of menu_view"""
    # set current menu and its categories
    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()
    
    # set current category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    # add to basket if want
    if quantity == 1:
        dish = Dish.objects.get(pk=dish_pk)
        if Dish_in_basket.objects.filter(name=dish):
            d = Dish_in_basket.objects.get(name=dish)
            d.quantity += 1
            d.save()   
        else:
            Dish_in_basket.objects.create(name=dish, quantity=1)

    # count number of dishes in basket
    count_dishes = []
    for dish in Dish_in_basket.objects.all():
        count_dishes.append(dish.quantity)
    count_dishes = sum(count_dishes)

    # count number of pieces in basket
    count_pieces = []
    for dish in Dish_in_basket.objects.all():
        quantity = Dish.objects.get(name=dish).amount
        how_many = dish.quantity
        count_pieces.append(quantity * how_many)
    count_pieces = sum(count_pieces)

    # assume cost of basket
    count_costs = []
    for dish in Dish_in_basket.objects.all():
        price = Dish.objects.get(name=dish).price
        how_many = dish.quantity
        count_costs.append(price * how_many)
    count_costs = sum(count_costs)

    # count for how many people is food in basket
    count_portion = []
    for dish in Dish_in_basket.objects.all():
        portion = Dish.objects.get(name=dish).portion_for
        how_many = dish.quantity
        count_portion.append(portion * how_many)
    count_portion = int(sum(count_portion))


    context =  {'menu'        :   menu,
                'categories'  :   categories,
                'category'    :   selected_category,
                'dishes'      :   dishes,
                'count_dishes':   count_dishes,
                'count_pieces':   count_pieces,
                'count_costs' :   count_costs,
                'count_portion':  count_portion,
                }
    return render(request, 'menu/menu.html', context)

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Menu, Category, Dish, Dish_in_basket, Basket


# Create your views here.
def index(request):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    
    # create new basket and save its pk in session
    basket = Basket()
    basket.save()
    basket_pk = basket.pk  
    request.session['basket_pk']=basket_pk

    context = {
        'menus' :   menus,
    }
    return render(request, 'menu/index.html', context)

def change_menu(request, basket_pk=None):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    
    request.session['basket_pk']=basket_pk

    context = {
        'menus' :   menus,
    }
    return render(request, 'menu/index.html', context)

def menu(request, menu_pk=1, category_pk=1, dish_pk_or_name = '0', quantity = 0, show_basket=False, show_similar=False):
    """ all behavior of menu_view"""

    # set current menu and its categories
    menu = Menu.objects.get(pk=menu_pk) 
    categories = menu.categories.all()
    
    # set current category to display dishes, default is first cat of specific menu
    selected_category = Category.objects.get(pk=category_pk)
    dishes = list(selected_category.dishes.all())

    # to do: refactor attribute's types
    if dish_pk_or_name == '0':
        dish_pk_or_name = selected_category.dishes.first().pk


    basket_pk=request.session['basket_pk']

    # add to basket either from menu or from basket
    if quantity == 1: # I want to add to basket
        try:
            dish_pk_or_name = int(dish_pk_or_name) # it is dish_pk when we add from menu
            dish = Dish.objects.get(pk=dish_pk_or_name)
            if Dish_in_basket.objects.filter(name=dish, basket_pk=basket_pk): # if is in basket
                d = Dish_in_basket.objects.get(name=dish, basket_pk=basket_pk)
                d.quantity += 1
                d.save()  
            else:   # if not in basket
                Dish_in_basket.objects.create(name=dish, quantity=1, basket_pk=basket_pk)
           
        except:
            dish = Dish.objects.get(name=dish_pk_or_name) # it is dish_name when we add from basket
            d = Dish_in_basket.objects.get(name=dish, basket_pk=basket_pk)
            d.quantity += 1
            d.save()
            
    elif quantity == 2: # if I want to remove from basket
        dish = Dish.objects.get(name=dish_pk_or_name)
        d = Dish_in_basket.objects.get(name=dish, basket_pk=basket_pk)
        if d.quantity > 0:
            d.quantity -= 1
            d.save()
    else:
        try:
            dish = Dish.objects.get(pk=dish_pk_or_name)
        except:
            dish = Dish.objects.get(name=dish_pk_or_name)

    basket = Dish_in_basket.objects.filter(basket_pk=basket_pk)

    """ here is needed refactor - repeat yourself """
    # count number of dishes in basket
    count_dishes = []
    for dish_in_basket in basket:
        count_dishes.append(dish_in_basket.quantity)
    count_dishes = sum(count_dishes)

    # count number of pieces in basket
    count_pieces = []
    for dish_in_basket in basket:
        quantity = Dish.objects.get(name=dish_in_basket).amount
        how_many = dish_in_basket.quantity
        count_pieces.append(quantity * how_many)
    count_pieces = sum(count_pieces)
    
    # assume cost of basket
    count_costs = []
    for dish_in_basket in basket:
        price = Dish.objects.get(name=dish_in_basket).price
        how_many = dish_in_basket.quantity
        count_costs.append(price * how_many)
    count_costs = sum(count_costs)

    # count for how many people is food in basket
    count_portion = []
    for dish_in_basket in basket:
        portion = Dish.objects.get(name=dish_in_basket).portion_for
        how_many = dish_in_basket.quantity
        count_portion.append(portion * how_many)
    count_portion = int(round(sum(count_portion)))

    
    context =  {'menu'        :   menu,
                'categories'  :   categories,
                'category'    :   selected_category,
                'dish_pk_or_name'     :   dish_pk_or_name,
                'dish'        :   dish,
                'dishes'      :   dishes,
                'basket'      :   basket,
                'basket_pk'   :   basket_pk,   
                'count_dishes':   count_dishes,
                'count_pieces':   count_pieces,
                'count_costs' :   count_costs,
                'count_portion':  count_portion,
                'show_basket' :   show_basket,
                'show_similar':   show_similar,
                }
    return render(request, 'menu/menu.html', context)

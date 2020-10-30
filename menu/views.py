from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    """ main page with logo, menu choice and account link in the future """
    menus = Menu.objects.all()
    return render(request, 'menu/index.html', {'menus':menus})

def menu(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    return render(request, 'menu/menu.html', {'menu':menu})
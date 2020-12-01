from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:basket_pk>', views.change_menu, name='change_menu'),
    path('menu/<int:menu_pk><int:category_pk>dish_<dish_pk_or_name><int:quantity>show_basket=<str:show_basket>show_similar=<str:show_similar>/', views.menu, name='menu'),
]
from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:menu_pk>/<int:category_pk>', views.menu, name='menu'),
    path('add_to_basket/<int:menu_pk>/<int:category_pk>/<int:dish_pk>/', views.add_to_basket, name='add_to_basket')
]
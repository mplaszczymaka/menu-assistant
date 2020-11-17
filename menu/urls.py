from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:menu_pk>/<int:category_pk>/<int:dish_pk>/<int:quantity>/<str:show_basket>/', views.menu, name='menu'),
]
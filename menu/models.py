from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """ can be in many dishes """
    name = models.CharField(max_length=30)
    available = models.BooleanField(default=True)

class Dish(models.Model):
    name = models.CharField(max_length=50)
    price = models.SmallIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    amount = models.SmallIntegerField()
    img = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=30)
    dishes = models.ManyToManyField(Dish)
    description = models.CharField(max_length=200)

class Menu(models.Model):
    # there must be one main menu and may be few specials
    name = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category)
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """ can be in many dishes """
    name = models.CharField(max_length=30)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    price = models.SmallIntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    amount = models.SmallIntegerField()
    # img = models.ImageField()

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    dishes = models.ManyToManyField(Dish)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Menu(models.Model):
    # there must be one main menu and may be few specials
    name = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.name).lower()
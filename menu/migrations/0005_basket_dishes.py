# Generated by Django 3.1.2 on 2020-11-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_basket_dishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='dishes',
            field=models.ManyToManyField(to='menu.Dish'),
        ),
    ]
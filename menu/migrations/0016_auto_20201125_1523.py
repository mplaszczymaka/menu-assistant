# Generated by Django 3.1.2 on 2020-11-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_dish_in_basket_basket_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish_in_basket',
            name='basket_pk',
            field=models.IntegerField(default=1),
        ),
    ]

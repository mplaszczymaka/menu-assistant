# Generated by Django 3.1.2 on 2020-11-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='dishes',
        ),
        migrations.AddField(
            model_name='basket',
            name='dishes',
            field=models.ManyToManyField(to='menu.Dish'),
        ),
    ]

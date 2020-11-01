# Generated by Django 3.1.2 on 2020-11-01 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'Dishes'},
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='available',
            new_name='is_available',
        ),
    ]
# Generated by Django 2.2.12 on 2020-11-16 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20201116_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='short_name',
        ),
    ]
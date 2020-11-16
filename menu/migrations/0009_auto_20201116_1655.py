# Generated by Django 2.2.12 on 2020-11-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_dish_portion_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='short_name',
            field=models.CharField(default=models.CharField(max_length=50), max_length=15),
        ),
        migrations.AlterField(
            model_name='dish',
            name='portion_for',
            field=models.DecimalField(decimal_places=1, default=0.7, max_digits=2),
        ),
    ]
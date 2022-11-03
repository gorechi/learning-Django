# Generated by Django 4.1 on 2022-10-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shawa_base', '0003_ingredient_shawa'),
    ]

    operations = [
        migrations.AddField(
            model_name='shawa',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Цена'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-05 23:16

import apartments.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_alter_apartment_added_date_alter_apartment_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='owner_phone_number',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='space',
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor_number',
            field=models.IntegerField(default=1, verbose_name='floor number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='size',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartment',
            name='bathrooms',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='bathrooms'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='beds',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='beds'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rooms',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='rooms'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='year_of_construction',
            field=models.IntegerField( verbose_name='year of construction'),
        ),
    ]
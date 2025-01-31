# Generated by Django 5.0.3 on 2024-04-05 22:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_alter_apartment_description_alter_apartment_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='added date'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='address',
            field=models.CharField(max_length=255, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='bathrooms',
            field=models.IntegerField(verbose_name='bathrooms'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='beds',
            field=models.IntegerField(verbose_name='beds'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='finishing_type',
            field=models.CharField(max_length=255, verbose_name='finishing type'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='owner_phone_number',
            field=models.CharField(max_length=20, verbose_name='owner phone number'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rooms',
            field=models.IntegerField(verbose_name='rooms'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='space',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='space'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated date'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='view',
            field=models.CharField(blank=True, max_length=255, verbose_name='view'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='year_of_construction',
            field=models.IntegerField(verbose_name='year of construction'),
        ),
    ]

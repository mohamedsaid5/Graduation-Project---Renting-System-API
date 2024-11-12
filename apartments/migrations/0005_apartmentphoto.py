# Generated by Django 5.0.3 on 2024-04-06 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_remove_apartment_owner_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='apartment_photos/')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='apartments.apartment')),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_governorate',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='birth_governorate'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]

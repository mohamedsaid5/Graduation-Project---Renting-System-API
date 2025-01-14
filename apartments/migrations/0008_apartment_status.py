# Generated by Django 5.0.3 on 2024-07-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_savedapartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('pending', 'Pending Approval'), ('published', 'Published'), ('denied', 'Denied')], default='pending', max_length=10),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-04 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

# Generated by Django 4.0 on 2022-06-07 21:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='Image',
            field=models.ImageField(default=datetime.datetime(2022, 6, 7, 21, 42, 28, 280281, tzinfo=utc), upload_to='static/Sell_images'),
        ),
    ]

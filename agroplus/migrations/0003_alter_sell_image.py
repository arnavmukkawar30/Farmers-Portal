# Generated by Django 4.0 on 2022-06-07 21:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0002_sell_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='Image',
            field=models.ImageField(default=datetime.datetime(2022, 6, 7, 21, 46, 38, 855511, tzinfo=utc), upload_to='static/Sell_images'),
        ),
    ]

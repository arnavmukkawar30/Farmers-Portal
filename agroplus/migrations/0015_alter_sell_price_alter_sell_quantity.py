# Generated by Django 4.0 on 2022-06-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0014_alter_sell_image_alter_sell_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='Price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sell',
            name='Quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

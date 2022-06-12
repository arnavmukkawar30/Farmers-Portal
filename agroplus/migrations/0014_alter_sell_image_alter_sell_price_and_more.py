# Generated by Django 4.0 on 2022-06-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0013_alter_sell_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='Image',
            field=models.ImageField(default='static/Sell_images/AGROPLUS.png', upload_to='static/Sell_images'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sell',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]

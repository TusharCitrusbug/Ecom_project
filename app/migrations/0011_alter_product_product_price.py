# Generated by Django 4.0.3 on 2022-03-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_shop_name_sellers_shop_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

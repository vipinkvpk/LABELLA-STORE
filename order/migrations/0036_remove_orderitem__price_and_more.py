# Generated by Django 5.0.4 on 2024-08-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0035_remove_orderitem_image_remove_orderitem_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='_price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='_product_name',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/order_items'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_price',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.4 on 2024-07-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0026_alter_returnorder_return_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon_discount',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]

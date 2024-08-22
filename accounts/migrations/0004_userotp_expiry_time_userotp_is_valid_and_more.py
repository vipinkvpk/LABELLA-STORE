# Generated by Django 5.0.4 on 2024-07-30 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='userotp',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 16, 41, 33, 100990, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userotp',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userotp',
            name='time_st',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
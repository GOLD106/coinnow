# Generated by Django 3.2.8 on 2022-11-22 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0008_auto_20221123_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productuserrelation',
            name='productIsSell',
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 8, 41, 52, 381319)),
        ),
        migrations.AlterField(
            model_name='sellhistory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 8, 41, 52, 385070)),
        ),
    ]

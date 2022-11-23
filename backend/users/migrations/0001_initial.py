# Generated by Django 3.2.8 on 2022-11-18 14:24

import backend.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('password', models.TextField()),
                ('balance', models.FloatField()),
                ('phone_number', models.DecimalField(decimal_places=0, max_digits=20)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to=backend.users.models.upload_to)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-16 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180516_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='media/image/upload.png', upload_to='image/%Y/%m'),
        ),
    ]

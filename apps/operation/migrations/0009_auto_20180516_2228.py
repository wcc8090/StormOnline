# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-16 22:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_auto_20180516_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-17 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0013_coursecomments_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_comment', to='operation.CourseComments'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_comment', to='operation.CourseComments'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160324_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='vote',
            field=models.CharField(choices=[('down', 'downvote'), ('up', 'upvote')], max_length=2, null=True),
        ),
    ]

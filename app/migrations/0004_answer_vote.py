# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160324_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.CharField(choices=[('up', 'upvote'), ('down', 'downvote')], max_length=2, null=True),
        ),
    ]

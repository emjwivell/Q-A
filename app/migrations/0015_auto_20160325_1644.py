# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_question_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(null=True, to='app.Answer'),
        ),
    ]
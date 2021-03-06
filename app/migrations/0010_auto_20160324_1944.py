# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160324_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=10)),
                ('downvote', models.IntegerField(default=-5)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='vote',
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Answer'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.ManyToManyField(through='app.Vote', to='app.UserProfile'),
        ),
    ]

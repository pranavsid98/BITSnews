# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newshome', '0005_auto_20161015_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PollC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PollQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_question', models.CharField(max_length=200)),
                ('poll_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='pollc',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newshome.PollQ'),
        ),
    ]

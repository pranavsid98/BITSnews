# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20161107_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_text', models.CharField(max_length=100)),
            ],
        ),
    ]
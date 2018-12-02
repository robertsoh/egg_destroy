# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('score_ms', models.FloatField(verbose_name='Score en milisegundos')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

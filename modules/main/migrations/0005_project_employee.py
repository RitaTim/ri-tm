# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-22 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170422_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Employee', verbose_name='Исполнитель'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170420_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='perсent',
            new_name='percent',
        ),
    ]
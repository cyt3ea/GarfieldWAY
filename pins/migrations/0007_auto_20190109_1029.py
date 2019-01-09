# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-09 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0006_auto_20190109_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_type',
            field=models.CharField(choices=[('c', 'Club'), ('p', 'Public'), ('r', 'Private'), ('o', 'Other')], max_length=1),
        ),
    ]

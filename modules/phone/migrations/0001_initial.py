# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-30 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(db_column='id_phone', primary_key=True, serialize=False)),
                ('number', models.CharField(db_column='number', max_length=500)),
                ('type', models.IntegerField(db_column='type')),
            ],
            options={
                'db_table': 'phone',
                'managed': True,
                'default_permissions': ('view',),
            },
        ),
    ]

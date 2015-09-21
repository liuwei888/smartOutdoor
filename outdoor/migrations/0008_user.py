# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0007_scene_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('telphone', models.CharField(max_length=100)),
                ('bankcard_num', models.CharField(max_length=100)),
                ('user_type', models.IntegerField()),
                ('user_score', models.IntegerField()),
                ('user_level', models.IntegerField()),
            ],
        ),
    ]

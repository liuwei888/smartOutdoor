# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0013_merchant_merchant_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scene_name', models.CharField(max_length=100)),
                ('scene_keyword', models.CharField(max_length=100)),
                ('scene_score', models.FloatField(max_length=100)),
                ('scene_comment_num', models.CharField(max_length=100)),
                ('scene_price', models.CharField(max_length=100)),
                ('scene_provience', models.CharField(max_length=100)),
                ('scene_imagepath', models.CharField(max_length=100)),
                ('scene_lon', models.CharField(max_length=100)),
                ('scene_lat', models.CharField(max_length=100)),
                ('scene_category', models.IntegerField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0005_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scene_name', models.CharField(max_length=100)),
                ('scene_keywords', models.TextField()),
                ('scene_score', models.FloatField()),
                ('scene_place', models.CharField(max_length=100)),
                ('scene_price', models.FloatField()),
                ('scene_opentime', models.DateTimeField()),
                ('scene_introduce', models.TextField()),
                ('scene_activity_type', models.IntegerField()),
                ('scene_imagepath', models.CharField(max_length=100)),
                ('scene_videopath', models.CharField(max_length=100)),
            ],
        ),
    ]

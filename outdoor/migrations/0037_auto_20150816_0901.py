# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0036_scene_scene_telphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene_item',
            name='scene_lat',
        ),
        migrations.RemoveField(
            model_name='scene_item',
            name='scene_lon',
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_lat',
            field=models.FloatField(default=0.0, verbose_name='\u7eac\u5ea6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_lon',
            field=models.FloatField(default=0.0, verbose_name='\u7ecf\u5ea6'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0019_auto_20150727_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene_item',
            name='scene_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_lon',
            field=models.FloatField(),
        ),
    ]

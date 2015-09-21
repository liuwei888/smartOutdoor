# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0025_remove_scene_item_scene_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

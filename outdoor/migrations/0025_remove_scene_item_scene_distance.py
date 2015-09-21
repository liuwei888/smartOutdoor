# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0024_scene_item_scene_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene_item',
            name='scene_distance',
        ),
    ]

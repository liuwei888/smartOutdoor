# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0050_remove_scene_scene_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_type',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_type_name',
        ),
    ]

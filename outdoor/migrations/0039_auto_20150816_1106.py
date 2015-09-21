# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0038_scene_scene_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene',
            name='scene_keywords',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='scene_name',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='scene_score',
        ),
    ]

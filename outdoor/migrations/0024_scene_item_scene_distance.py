# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0023_auto_20150728_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene_item',
            name='scene_distance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

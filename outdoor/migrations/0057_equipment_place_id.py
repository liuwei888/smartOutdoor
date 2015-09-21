# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0056_remove_equipment_scene_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='place_id',
            field=models.IntegerField(default=1, verbose_name='\u666f\u70b9ID'),
            preserve_default=False,
        ),
    ]

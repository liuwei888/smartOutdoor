# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0014_scene_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_owner',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]

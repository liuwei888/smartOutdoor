# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0018_equipment_equipment_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

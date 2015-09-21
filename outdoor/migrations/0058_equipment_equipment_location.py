# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0057_equipment_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_location',
            field=models.CharField(default='wuhan', max_length=100, verbose_name='\u8bbe\u5907\u6240\u5728\u5730'),
            preserve_default=False,
        ),
    ]

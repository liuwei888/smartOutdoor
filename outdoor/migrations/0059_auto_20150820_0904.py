# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0058_equipment_equipment_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_order',
            name='end_time',
            field=models.CharField(max_length=100, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='start_time',
            field=models.CharField(max_length=100, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]

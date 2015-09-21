# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0059_auto_20150820_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_order',
            name='end_time',
            field=models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='start_time',
            field=models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]

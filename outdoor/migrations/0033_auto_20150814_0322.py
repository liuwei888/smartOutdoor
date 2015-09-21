# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0032_auto_20150814_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment_order',
            name='end_time',
            field=models.DateTimeField(verbose_name='\u9884\u5b9a\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='equipment_id',
            field=models.IntegerField(verbose_name='\u8bbe\u5907ID'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='start_time',
            field=models.DateTimeField(verbose_name='\u9884\u5b9a\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='user_id',
            field=models.IntegerField(verbose_name='\u7528\u6237ID'),
        ),
    ]

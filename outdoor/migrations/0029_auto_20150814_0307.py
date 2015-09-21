# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0028_auto_20150814_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_category',
            name='end_time',
            field=models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='activity_category',
            name='equipment_id',
            field=models.IntegerField(verbose_name='\u8bbe\u5907ID'),
        ),
        migrations.AlterField(
            model_name='activity_category',
            name='start_time',
            field=models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='activity_category',
            name='user_id',
            field=models.IntegerField(verbose_name='\u7528\u6237ID'),
        ),
    ]

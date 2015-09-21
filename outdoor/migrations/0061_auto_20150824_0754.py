# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0060_auto_20150820_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_owner',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u6240\u5c5e\u8005'),
        ),
    ]

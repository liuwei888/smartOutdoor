# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0051_auto_20150819_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_owner',
            field=models.IntegerField(verbose_name='\u8bbe\u5907\u6240\u5c5e\u8005'),
        ),
    ]

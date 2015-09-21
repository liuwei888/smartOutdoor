# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0053_auto_20150819_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='merchant_id',
            field=models.IntegerField(default=0, verbose_name='\u5546\u6237ID'),
            preserve_default=False,
        ),
    ]

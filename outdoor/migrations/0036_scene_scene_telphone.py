# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0035_auto_20150814_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='scene_telphone',
            field=models.CharField(default='00000000', max_length=100, verbose_name='\u8054\u7cfb\u65b9\u5f0f'),
            preserve_default=False,
        ),
    ]

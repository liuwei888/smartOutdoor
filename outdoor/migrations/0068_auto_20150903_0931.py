# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0067_user_video_video_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_order',
            name='equipment_name',
            field=models.CharField(default='null', max_length=100, verbose_name='\u8bbe\u5907\u540d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_order',
            name='equipment_price',
            field=models.FloatField(default=0.0, verbose_name='\u8bbe\u5907\u4ef7\u683c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_order',
            name='state',
            field=models.CharField(default='null', max_length=100, verbose_name='\u72b6\u6001'),
            preserve_default=False,
        ),
    ]

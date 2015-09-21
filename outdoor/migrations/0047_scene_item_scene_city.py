# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0046_scene_markicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene_item',
            name='scene_city',
            field=models.CharField(default='wuhan', max_length=100, verbose_name='\u6240\u5728\u57ce\u5e02'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0039_auto_20150816_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene_item',
            name='scene_provience',
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_provience',
            field=models.CharField(default='hubei', max_length=100, verbose_name='\u6240\u5c5e\u7701\u4efd'),
            preserve_default=False,
        ),
    ]

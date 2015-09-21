# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0042_auto_20150817_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='scene_imagepath1',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u72471'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_imagepath2',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u72472'),
        ),
    ]

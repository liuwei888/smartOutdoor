# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0044_auto_20150817_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='scene_imagepath2',
            field=models.CharField(max_length=1000, verbose_name='\u56fe\u72472'),
        ),
    ]

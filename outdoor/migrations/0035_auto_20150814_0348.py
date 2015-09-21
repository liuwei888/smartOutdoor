# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0034_auto_20150814_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='scene_imagepath',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_introduce',
            field=models.TextField(verbose_name='\u4ecb\u7ecd'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_videopath',
            field=models.CharField(max_length=100, verbose_name='\u89c6\u9891'),
        ),
    ]

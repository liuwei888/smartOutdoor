# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0041_auto_20150817_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scene',
            old_name='scene_imagepath',
            new_name='scene_imagepath1',
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_imagepath2',
            field=models.CharField(default='null', max_length=100, verbose_name='\u56fe\u7247'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0063_user_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_album',
            name='photo_describe',
            field=models.CharField(default='null', max_length=100, verbose_name='\u76f8\u7247\u63cf\u8ff0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_video',
            name='video_describe',
            field=models.CharField(default='null', max_length=100, verbose_name='\u89c6\u9891\u63cf\u8ff0'),
            preserve_default=False,
        ),
    ]

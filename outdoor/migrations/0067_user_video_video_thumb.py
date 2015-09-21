# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0066_user_album_photo_mapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_video',
            name='video_thumb',
            field=models.CharField(default='null', max_length=100, verbose_name='\u7f29\u7565\u56fe'),
            preserve_default=False,
        ),
    ]

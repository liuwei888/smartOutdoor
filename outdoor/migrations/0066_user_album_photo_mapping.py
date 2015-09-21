# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0065_user_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_album',
            name='photo_mapping',
            field=models.CharField(default='null', max_length=100, verbose_name='\u6620\u5c04'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0037_auto_20150816_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='scene_id',
            field=models.IntegerField(default=0, verbose_name='\u666f\u70b9ID'),
            preserve_default=False,
        ),
    ]

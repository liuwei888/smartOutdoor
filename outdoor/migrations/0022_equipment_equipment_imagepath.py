# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0021_auto_20150727_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_imagepath',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]

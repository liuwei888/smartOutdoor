# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0020_auto_20150727_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_beordered',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 22, 5, 33, 959902, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 22, 5, 41, 54767, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

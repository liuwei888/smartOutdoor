# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0052_auto_20150819_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_beordered',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_endtime',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='equipment_starttime',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0049_auto_20150818_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene',
            name='scene_location',
        ),
    ]

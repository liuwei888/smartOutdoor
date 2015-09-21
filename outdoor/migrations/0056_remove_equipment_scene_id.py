# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0055_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='scene_id',
        ),
    ]

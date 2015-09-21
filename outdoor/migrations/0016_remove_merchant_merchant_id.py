# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0015_equipment_equipment_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='merchant_id',
        ),
    ]

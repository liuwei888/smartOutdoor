# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0017_equipment_equipment_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_type_name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]

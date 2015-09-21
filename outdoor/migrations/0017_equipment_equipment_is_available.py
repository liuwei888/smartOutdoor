# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0016_remove_merchant_merchant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_is_available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

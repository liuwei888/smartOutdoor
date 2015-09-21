# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0012_auto_20150726_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='merchant_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

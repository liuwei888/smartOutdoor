# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0009_merchant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]

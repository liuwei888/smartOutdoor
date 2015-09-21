# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0011_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='merchant_intro',
            field=models.TextField(),
        ),
    ]

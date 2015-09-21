# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0030_auto_20150814_0314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity_category',
            options={'verbose_name_plural': '\u6d3b\u52a8\u79cd\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name_plural': '\u8bbe\u5907'},
        ),
    ]

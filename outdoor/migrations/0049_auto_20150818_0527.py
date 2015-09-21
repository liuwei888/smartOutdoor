# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0048_auto_20150818_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='scene_location',
            field=models.CharField(max_length=100, verbose_name='\u666f\u70b9\u6240\u5728\u5730'),
        ),
    ]

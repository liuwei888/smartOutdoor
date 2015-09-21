# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0040_auto_20150816_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='scene_opentime',
            field=models.CharField(max_length=100, verbose_name='\u5f00\u653e\u65f6\u95f4'),
        ),
    ]

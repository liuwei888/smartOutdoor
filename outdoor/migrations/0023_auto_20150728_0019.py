# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0022_equipment_equipment_imagepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_is_available',
            field=models.CharField(max_length=100),
        ),
    ]

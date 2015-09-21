# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0026_equipment_equipment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_id', models.IntegerField()),
                ('place_name', models.CharField(max_length=100)),
            ],
        ),
    ]

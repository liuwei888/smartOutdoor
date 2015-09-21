# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0003_equipment_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.IntegerField()),
                ('product_photo', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_num', models.IntegerField()),
                ('product_introduce', models.TextField()),
            ],
        ),
    ]

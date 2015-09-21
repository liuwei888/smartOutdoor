# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0064_auto_20150824_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name='\u7528\u6237ID')),
                ('equipment_id', models.IntegerField(verbose_name='\u8bbe\u5907ID')),
                ('order_time', models.CharField(max_length=100, verbose_name='\u8ba2\u5355\u65f6\u95f4')),
                ('order_remark', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
                ('number', models.IntegerField(verbose_name='\u6570\u91cf')),
            ],
            options={
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
    ]

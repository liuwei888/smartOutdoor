# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0062_auto_20150824_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name='\u7528\u6237ID')),
                ('video_name', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d\u79f0')),
                ('video_path', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u8def\u5f84')),
            ],
            options={
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]

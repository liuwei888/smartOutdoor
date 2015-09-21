# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0061_auto_20150824_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name='\u7528\u6237ID')),
                ('album_name', models.CharField(max_length=100, verbose_name='\u76f8\u518c\u540d\u79f0')),
                ('photo_path', models.CharField(max_length=100, verbose_name='\u76f8\u7247\u8def\u5f84')),
            ],
            options={
                'verbose_name_plural': '\u7167\u7247',
            },
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='merchant_id',
        ),
    ]

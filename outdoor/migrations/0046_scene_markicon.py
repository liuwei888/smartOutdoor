# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0045_auto_20150817_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene_markicon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scene_id', models.IntegerField(verbose_name='\u666f\u70b9ID')),
                ('scene_icon', models.CharField(max_length=100, verbose_name='\u666f\u70b9\u56fe\u6807')),
            ],
            options={
                'verbose_name_plural': '\u666f\u70b9\u6807\u6ce8',
            },
        ),
    ]

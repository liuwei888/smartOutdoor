# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0006_scene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene_comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('scene_id', models.IntegerField()),
                ('comment', models.TextField()),
                ('submit_time', models.DateTimeField()),
            ],
        ),
    ]

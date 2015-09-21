# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0047_scene_item_scene_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scene',
            old_name='scene_provience',
            new_name='scene_location',
        ),
    ]

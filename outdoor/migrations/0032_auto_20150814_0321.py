# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0031_auto_20150814_0315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment_order',
            options={'verbose_name_plural': '\u8bbe\u5907\u8ba2\u5355'},
        ),
        migrations.AlterModelOptions(
            name='merchant',
            options={'verbose_name_plural': '\u5546\u6237'},
        ),
        migrations.AlterModelOptions(
            name='place_category',
            options={'verbose_name_plural': '\u573a\u6240\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '\u4ea7\u54c1'},
        ),
        migrations.AlterModelOptions(
            name='product_category',
            options={'verbose_name_plural': '\u4ea7\u54c1\u79cd\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='scene',
            options={'verbose_name_plural': '\u573a\u666f'},
        ),
        migrations.AlterModelOptions(
            name='scene_comment',
            options={'verbose_name_plural': '\u573a\u666f\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='scene_item',
            options={'verbose_name_plural': '\u573a\u666f\u6761\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '\u7528\u6237'},
        ),
    ]

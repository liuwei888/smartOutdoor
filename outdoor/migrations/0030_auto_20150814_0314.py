# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0029_auto_20150814_0307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': '\u8bbe\u5907'},
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_beordered',
            field=models.CharField(max_length=100, verbose_name='\u88ab\u8c01\u9884\u5b9a'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_endtime',
            field=models.DateTimeField(verbose_name='\u79df\u7528\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_id',
            field=models.IntegerField(verbose_name='\u8bbe\u5907ID'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_imagepath',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u7247\u5b58\u653e\u8def\u5f84'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_intro',
            field=models.TextField(verbose_name='\u8bbe\u5907\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_is_available',
            field=models.CharField(max_length=100, verbose_name='\u662f\u5426\u53ef\u7528'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_lat',
            field=models.FloatField(verbose_name='\u8bbe\u5907\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_lon',
            field=models.FloatField(verbose_name='\u8bbe\u5907\u7ecf\u5ea6'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_name',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_owner',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u62e5\u6709\u8005'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_starttime',
            field=models.DateTimeField(verbose_name='\u79df\u7528\u8d77\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.IntegerField(verbose_name='\u8bbe\u5907\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type_name',
            field=models.CharField(max_length=200, verbose_name='\u8bbe\u5907\u7c7b\u578b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='scene_id',
            field=models.IntegerField(verbose_name='\u573a\u666fID'),
        ),
    ]

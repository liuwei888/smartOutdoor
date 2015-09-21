# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0033_auto_20150814_0322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scene',
            options={'verbose_name_plural': '\u666f\u70b9'},
        ),
        migrations.AlterModelOptions(
            name='scene_comment',
            options={'verbose_name_plural': '\u666f\u70b9\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='scene_item',
            options={'verbose_name_plural': '\u666f\u70b9\u6761\u76ee'},
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_endtime',
            field=models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_imagepath',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u7247\u8def\u5f84'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_lat',
            field=models.FloatField(verbose_name='\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_lon',
            field=models.FloatField(verbose_name='\u7ecf\u5ea6'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_owner',
            field=models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u6240\u5c5e\u8005'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_starttime',
            field=models.DateTimeField(verbose_name='\u8d77\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type_name',
            field=models.CharField(max_length=200, verbose_name='\u7c7b\u578b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='end_time',
            field=models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipment_order',
            name='start_time',
            field=models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_address',
            field=models.CharField(max_length=100, verbose_name='\u5546\u6237\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_company_name',
            field=models.CharField(max_length=100, verbose_name='\u5546\u6237\u516c\u53f8\u540d'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_email',
            field=models.CharField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_intro',
            field=models.TextField(verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_login_name',
            field=models.CharField(max_length=100, verbose_name='\u5546\u6237\u767b\u5f55\u540d'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_password',
            field=models.CharField(max_length=100, verbose_name='\u5546\u6237\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_telphone',
            field=models.CharField(max_length=100, verbose_name='\u8054\u7cfb\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='place_category',
            name='place_id',
            field=models.IntegerField(verbose_name='\u573a\u6240ID'),
        ),
        migrations.AlterField(
            model_name='place_category',
            name='place_name',
            field=models.CharField(max_length=100, verbose_name='\u573a\u6240\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_introduce',
            field=models.TextField(verbose_name='\u4ea7\u54c1\u4ecb\u7ecd'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_num',
            field=models.IntegerField(verbose_name='\u4ea7\u54c1\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_photo',
            field=models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(verbose_name='\u4ea7\u54c1\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.IntegerField(verbose_name='\u4ea7\u54c1\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='\u7c7b\u578b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_activity_type',
            field=models.IntegerField(verbose_name='\u6d3b\u52a8\u79cd\u7c7b'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_imagepath',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u7247\u8def\u5f84'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_introduce',
            field=models.TextField(verbose_name='\u666f\u70b9\u4ecb\u7ecd'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_keywords',
            field=models.TextField(verbose_name='\u5173\u952e\u5b57'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_name',
            field=models.CharField(max_length=100, verbose_name='\u666f\u70b9\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_opentime',
            field=models.DateTimeField(verbose_name='\u5f00\u653e\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_place',
            field=models.CharField(max_length=100, verbose_name='\u6240\u5728\u5730'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_price',
            field=models.FloatField(verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_score',
            field=models.FloatField(verbose_name='\u8bc4\u5206'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_videopath',
            field=models.CharField(max_length=100, verbose_name='\u89c6\u9891\u8def\u5f84'),
        ),
        migrations.AlterField(
            model_name='scene_comment',
            name='comment',
            field=models.TextField(verbose_name='\u8bc4\u8bba'),
        ),
        migrations.AlterField(
            model_name='scene_comment',
            name='scene_id',
            field=models.IntegerField(verbose_name='\u666f\u70b9ID'),
        ),
        migrations.AlterField(
            model_name='scene_comment',
            name='submit_time',
            field=models.DateTimeField(verbose_name='\u63d0\u4ea4\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='scene_comment',
            name='user_id',
            field=models.IntegerField(verbose_name='\u7528\u6237ID'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_category',
            field=models.IntegerField(verbose_name='\u666f\u70b9\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_comment_num',
            field=models.CharField(max_length=100, verbose_name='\u8bc4\u8bba\u6570'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_imagepath',
            field=models.CharField(max_length=100, verbose_name='\u56fe\u7247\u8def\u5f84'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_keyword',
            field=models.CharField(max_length=100, verbose_name='\u5173\u952e\u5b57'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_lat',
            field=models.FloatField(verbose_name='\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_lon',
            field=models.FloatField(verbose_name='\u7ecf\u5ea6'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_name',
            field=models.CharField(max_length=100, verbose_name='\u666f\u70b9\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_price',
            field=models.CharField(max_length=100, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_provience',
            field=models.CharField(max_length=100, verbose_name='\u6240\u5c5e\u7701\u4efd'),
        ),
        migrations.AlterField(
            model_name='scene_item',
            name='scene_score',
            field=models.FloatField(max_length=100, verbose_name='\u8bc4\u5206'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='\u5e74\u9f84'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bankcard_num',
            field=models.CharField(max_length=100, verbose_name='\u94f6\u884c\u5361\u53f7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=100, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telphone',
            field=models.CharField(max_length=100, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(verbose_name='\u7528\u6237\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_score',
            field=models.IntegerField(verbose_name='\u7528\u6237\u79ef\u5206'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(verbose_name='\u7528\u6237\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, verbose_name='\u7528\u6237\u540d'),
        ),
    ]

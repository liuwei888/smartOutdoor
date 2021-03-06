# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outdoor', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('merchant_name', models.CharField(max_length=100)),
                ('merchant_password', models.CharField(max_length=100)),
                ('merchant_email', models.CharField(max_length=100)),
                ('merchant_intro', models.TextField()),
                ('merchant_address', models.CharField(max_length=100)),
                ('merchant_telphone', models.CharField(max_length=100)),
            ],
        ),
    ]

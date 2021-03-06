# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EastMoneyTableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_time', models.DateTimeField()),
                ('bk_list_type', models.IntegerField()),
                ('sequence', models.IntegerField()),
                ('bk_name', models.CharField(blank=True, max_length=100)),
                ('last_price', models.FloatField()),
                ('raise_down', models.FloatField()),
                ('raise_down_perc', models.FloatField()),
                ('total_value', models.FloatField()),
                ('changes', models.FloatField()),
                ('raise_num', models.IntegerField()),
                ('down_num', models.IntegerField()),
                ('top_raise_down', models.CharField(blank=True, max_length=100)),
                ('top_raise_down_perc', models.FloatField()),
            ],
            options={
                'ordering': ('collection_time', 'sequence'),
            },
        ),
        migrations.CreateModel(
            name='JqkaTableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_time', models.DateTimeField()),
                ('sequence', models.IntegerField()),
                ('bk_name', models.CharField(blank=True, max_length=100)),
                ('fluctuation', models.FloatField()),
                ('total_count', models.FloatField()),
                ('total_fee', models.FloatField()),
                ('net_incoming', models.FloatField()),
                ('up_count', models.IntegerField()),
                ('down_count', models.IntegerField()),
                ('average', models.FloatField()),
                ('top_name', models.CharField(blank=True, max_length=100)),
                ('price', models.FloatField()),
                ('top_fluctuation', models.FloatField()),
            ],
            options={
                'ordering': ('collection_time', 'sequence'),
            },
        ),
    ]

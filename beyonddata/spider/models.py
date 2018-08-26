# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EastMoneyTableData(models.Model):
    collection_time = models.DateTimeField(auto_now_add=False)
    bk_list_type = models.IntegerField()
    sequence = models.IntegerField()
    bk_name = models.CharField(max_length=100, blank=True)
    last_price = models.FloatField()
    raise_down = models.FloatField()
    raise_down_perc = models.FloatField()
    total_value = models.FloatField()
    changes = models.FloatField()
    raise_num = models.IntegerField()
    down_num = models.IntegerField()
    top_raise_down = models.CharField(max_length=100, blank=True)
    top_raise_down_perc = models.FloatField()

    class Meta:
        ordering = ('collection_time','sequence')


class JqkaTableData(models.Model):
    collection_time = models.DateTimeField(auto_now_add=False)
    sequence = models.IntegerField()
    bk_name = models.CharField(max_length=100, blank=True)
    fluctuation = models.FloatField()
    total_count = models.FloatField()
    total_fee = models.FloatField()
    net_incoming = models.FloatField()
    up_count = models.IntegerField()
    down_count = models.IntegerField()
    average = models.FloatField()
    top_name = models.CharField(max_length=100, blank=True)
    price = models.FloatField()
    top_fluctuation = models.FloatField()

    class Meta:
        ordering = ('collection_time', 'sequence')

class EastMoneyAnalysisData(models.Model):
    time_seq = models.IntegerField()
    name_seq = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        ordering = ('time_seq')
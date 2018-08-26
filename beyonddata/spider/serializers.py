# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import *

class EastMoneyTableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EastMoneyTableData
        fields = ('collection_time', 'bk_list_type', 'sequence', 'bk_name', 'last_price', 'raise_down', 'raise_down_perc', 'total_value', 'changes', 'raise_num', 'down_num', 'top_raise_down', 'top_raise_down_perc')

class JqkaTableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JqkaTableData
        fields = ('collection_time', 'sequence', 'bk_name', 'fluctuation', 'total_count', 'total_fee', 'net_incoming', 'up_count', 'down_count', 'average', 'top_name', 'price', 'top_fluctuation')

class EastmoneyGnbkupAnalysisDataSerializer(serializers.ModelSerializer)
    class Meta:
        models = EastMoneyAnalysisData
        fields = ('time_seq', 'name_seq', 'count')

class EastmoneyGnbkupAnalysisTimeSerializer(serializers.ModelSerializer)
    class Meta:
        models = EastMoneyAnalysisData
        fields = ('time_seq')

class EastmoneyGnbkupAnalysisBKNameSerializer(serializers.ModelSerializer)
    class Meta:
        models = EastMoneyAnalysisData
        fields = ('name_seq')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import EastMoneyTableData, JqkaTableData
from serializers import EastMoneyTableDataSerializer, JqkaTableDataSerializer, EastmoneyGnbkupAnalysisDataSerializer, EastmoneyGnbkupAnalysisTimeSerializer, EastmoneyGnbkupAnalysisBKNameSerializer
from rest_framework import viewsets
from rest_framework import generics
import datetime
import pymysql.cursors
import pandas as pd

def con():
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='123456654321',
                                 db='QuantitativeTrading',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 connect_timeout=60)
    return  connection

# # Create your views here.
# def eastmoney_hybkup_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         eastmoney_hybkup_list = EastMoneyTableData.objects.all()
#         serializer = EastMoneyTableDataSerializer(eastmoney_hybkup_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
# def eastmoney_hybkup_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         eastmoney_hybkup_detail = EastMoneyTableData.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = EastMoneyTableDataSerializer(eastmoney_hybkup_detail)
#         return JsonResponse(serializer.data)

# select_time = datetime.date.today()
# if datetime.datetime.today().weekday() >= 5:
#     select_time = select_time + datetime.timedelta(4 - select_time.weekday())


class EastmoneyHybkupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer
    filter_fields = ('bk_list_type','collection_time')

    # def get_queryset(self):
    #     queryset = EastMoneyTableData.objects.all()
    #     queryset = queryset.filter(collection_time=select_time)
    #     return queryset



class EastmoneyHybkdownViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer
    filter_fields = ('bk_list_type', 'collection_time')


class EastmoneyGnbkupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer
    filter_fields = ('bk_list_type', 'collection_time')


class EastmoneyGnbkdownViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer
    filter_fields = ('bk_list_type', 'collection_time')

class JqkaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JqkaTableData.objects.all()
    serializer_class = JqkaTableDataSerializer
    filter_fields = ('collection_time')

class EastmoneyHybkupAnalysisView(generics.ListCreateAPIView):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer

    def list(self, request):
        conn = con()
        df = pd.read_sql(
            '''select DATE_FORMAT(collection_time,'%u') as weeks, count(bk_name) as count, bk_name from BKList where bk_list_type = 0 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df3 = pd.read_sql(
            '''select distinct DATE_FORMAT(collection_time,'%u') as weeks from BKList where bk_list_type = 0 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df2 = pd.read_sql(
            '''select distinct bk_name from BKList where bk_list_type = 0 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK);''',
            conn)

        conn.close()
        df2['name_seq'] = df2.index
        df3['time_seq'] = df3.index
        ts = pd.merge(pd.merge(df, df2, on='bk_name', how='left'), df3, on='weeks')
        ts = ts.loc[:, ['time_seq', 'name_seq', 'count']]
        data = {'name': df2['bk_name'].values.tolist(),'time':df3['weeks'].values.tolist(), 'combine':ts.values.tolist()}
        data_str = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        return Response(json.loads(data_str))

class EastmoneyHybkdownAnalysisView(generics.ListCreateAPIView):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer

    def list(self, request):
        conn = con()
        df = pd.read_sql(
            '''select DATE_FORMAT(collection_time,'%u') as weeks, count(bk_name) as count, bk_name from BKList where bk_list_type = 1 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df3 = pd.read_sql(
            '''select distinct DATE_FORMAT(collection_time,'%u') as weeks from BKList where bk_list_type = 1 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df2 = pd.read_sql(
            '''select distinct bk_name from BKList where bk_list_type = 1 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK);''',
            conn)

        conn.close()
        df2['name_seq'] = df2.index
        df3['time_seq'] = df3.index
        ts = pd.merge(pd.merge(df, df2, on='bk_name', how='left'), df3, on='weeks')
        ts = ts.loc[:, ['time_seq', 'name_seq', 'count']]
        data = {'name': df2['bk_name'].values.tolist(), 'time': df3['weeks'].values.tolist(), 'combine': ts.values.tolist()}
        data_str = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        return Response(json.loads(data_str))

class EastmoneyGnbkupAnalysisView(generics.ListCreateAPIView):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer

    def list(self, request):
        conn = con()
        df = pd.read_sql(
            '''select DATE_FORMAT(collection_time,'%u') as weeks, count(bk_name) as count, bk_name from BKList where bk_list_type = 2 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df3 = pd.read_sql(
            '''select distinct DATE_FORMAT(collection_time,'%u') as weeks from BKList where bk_list_type = 2 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df2 = pd.read_sql(
            '''select distinct bk_name from BKList where bk_list_type = 2 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK);''',
            conn)

        conn.close()
        df2['name_seq'] = df2.index
        df3['time_seq'] = df3.index
        ts = pd.merge(pd.merge(df, df2, on='bk_name', how='left'), df3, on='weeks')
        ts = ts.loc[:, ['time_seq', 'name_seq', 'count']]
        data = {'name': df2['bk_name'].values.tolist(), 'time': df3['weeks'].values.tolist(), 'combine': ts.values.tolist()}
        data_str = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        return Response(json.loads(data_str))

class EastmoneyGnbkdownAnalysisView(generics.ListCreateAPIView):
    queryset = EastMoneyTableData.objects.all()
    serializer_class = EastMoneyTableDataSerializer

    def list(self, request):
        conn = con()
        df = pd.read_sql(
            '''select DATE_FORMAT(collection_time,'%u') as weeks, count(bk_name) as count, bk_name from BKList where bk_list_type = 3 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df3 = pd.read_sql(
            '''select distinct DATE_FORMAT(collection_time,'%u') as weeks from BKList where bk_list_type = 3 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df2 = pd.read_sql(
            '''select distinct bk_name from BKList where bk_list_type = 3 and YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK);''',
            conn)

        conn.close()
        df2['name_seq'] = df2.index
        df3['time_seq'] = df3.index
        ts = pd.merge(pd.merge(df, df2, on='bk_name', how='left'), df3, on='weeks')
        ts = ts.loc[:, ['time_seq', 'name_seq', 'count']]
        data = {'name': df2['bk_name'].values.tolist(), 'time': df3['weeks'].values.tolist(), 'combine': ts.values.tolist()}
        data_str = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        return Response(json.loads(data_str))

class JqkabkupAnalysisView(generics.ListCreateAPIView):
    queryset = JqkaTableData.objects.all()
    serializer_class = JqkaTableDataSerializer

    def list(self, request):
        conn = con()
        df = pd.read_sql(
            '''select DATE_FORMAT(collection_time,'%u') as weeks, count(bk_name) as count, bk_name from HYList where YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df3 = pd.read_sql(
            '''select distinct DATE_FORMAT(collection_time,'%u') as weeks from HYList where YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK) group by weeks, bk_name;''',
            conn)
        df2 = pd.read_sql(
            '''select distinct bk_name from HYList where YEARWEEK(date_format(collection_time,'%Y-%m-%d')) > YEARWEEK(CURDATE() - INTERVAL 8 WEEK);''',
            conn)

        conn.close()
        df2['name_seq'] = df2.index
        df3['time_seq'] = df3.index
        ts = pd.merge(pd.merge(df, df2, on='bk_name', how='left'), df3, on='weeks')
        ts = ts.loc[:, ['time_seq', 'name_seq', 'count']]
        data = {'name': df2['bk_name'].values.tolist(), 'time': df3['weeks'].values.tolist(), 'combine': ts.values.tolist()}
        data_str = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        return Response(json.loads(data_str))

# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import PublicArticle, Tag, Classification
from serializers import PublicArticleSerializer, TagSerializer, PublicArticleListSerializer, ClassificationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework.decorators import detail_route, list_route
# from rest_framework.response import Response
# from rest_framework import status


class PublicArticleViewSet(viewsets.ModelViewSet):
    queryset = PublicArticle.objects.all()
    serializer_class = PublicArticleSerializer

    def list(self, request):
        queryset = PublicArticle.objects.all()
        username = self.request.query_params.get('owner', None)
        if username is not None:
            queryset = queryset.filter(owner__username=username)
        serializer = PublicArticleListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PublicArticle.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = PublicArticleSerializer(article)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


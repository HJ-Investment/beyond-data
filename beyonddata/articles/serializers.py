# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import *


class PublicArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicArticle
        fields = ('article_title', 'content', 'tags', 'classification', 'is_top', 'finalUrl', 'owner', 'publish_time', 'save_time', 'is_published', 'is_draft', 'created_time')


class PublicArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicArticle
        fields = ('id','article_title','tags', 'classification', 'is_top', 'finalUrl', 'owner', 'publish_time', 'save_time', 'is_published', 'is_draft', 'created_time')



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','tag_name', 'created_time')

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('id', 'classification', 'created_time')
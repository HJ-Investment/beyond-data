# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from articles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', views.PublicArticleViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'classifications', views.ClassificationViewSet)


urlpatterns = [
        url(r'^', include(router.urls)),
]
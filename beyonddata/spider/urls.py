# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from spider import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'eastmoney_hybkup', views.EastmoneyHybkupViewSet)
router.register(r'eastmoney_hybkdown', views.EastmoneyHybkdownViewSet)
router.register(r'eastmoney_gnbkup', views.EastmoneyGnbkupViewSet)
router.register(r'eastmoney_gnbkdown', views.EastmoneyGnbkdownViewSet)
router.register(r'jqka', views.JqkaViewSet)

urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'eastmoneyhybkupanalysis', views.EastmoneyHybkupAnalysisView.as_view()),
        url(r'eastmoneyhybkdownanalysis', views.EastmoneyHybkdownAnalysisView.as_view()),
        url(r'eastmoneygnbkupanalysis', views.EastmoneyGnbkupAnalysisView.as_view()),
        url(r'eastmoneygnbkdownanalysis', views.EastmoneyGnbkdownAnalysisView.as_view()),
        url(r'jqkabkupanalysis', views.JqkabkupAnalysisView.as_view()),
]
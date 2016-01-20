# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name="list"),
    url(r'^create/$', views.ProjectCreateView.as_view(), name="create"),
]

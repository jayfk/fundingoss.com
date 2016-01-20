# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name="list"),
    url(r'^json/$', views.ProjectJSONView.as_view(), name="json"),
    url(r'^create/$', views.ProjectCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name="detail"),
]

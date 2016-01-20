# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic import ListView, CreateView
from .models import Project


class ProjectListView(ListView):
    template_name = "projects/list.html"
    context_object_name = "projects"
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ("name", "website", "languages", "function", "maintainers", "added", "needs",
              "funding_status", "funding_status_notes")

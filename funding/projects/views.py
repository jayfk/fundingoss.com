# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic import ListView, CreateView, DetailView
from .models import Project
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class ProjectListView(ListView):
    template_name = "projects/list.html"
    context_object_name = "projects"
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ("name", "website", "languages", "function", "maintainers", "added", "needs",
              "funding_status", "funding_status_notes")
    success_url = reverse_lazy("projects:list")

    def form_valid(self, form):
        messages.info(self.request, "Project added")
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDetailView(DetailView):

    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"

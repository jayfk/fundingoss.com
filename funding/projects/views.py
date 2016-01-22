# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic import ListView, CreateView, DetailView
from .models import Project
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from braces.views import JSONResponseMixin
from django.forms.models import model_to_dict


class ProjectListView(ListView):
    template_name = "projects/list.html"
    context_object_name = "projects"
    model = Project

    def get_context_data(self, **kwargs):
        data = super(ProjectListView, self).get_context_data(**kwargs)
        data["status_choices"] = Project.STATUS_CHOICES
        return data


class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ("name", "website", "languages", "function", "maintainers", "added", "needs",
              "funding_status", "funding_status_notes", "license")
    success_url = reverse_lazy("projects:list")

    def form_valid(self, form):
        messages.info(self.request, "Project added")
        return super(ProjectCreateView, self).form_valid(form)


class ProjectDetailView(DetailView):

    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project"


class ProjectJSONView(JSONResponseMixin, ProjectListView):

    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):
        context_dict = {
            "projects": [model_to_dict(project, exclude=["pk"]) for project in self.get_queryset()]
        }

        return self.render_json_response(context_dict)

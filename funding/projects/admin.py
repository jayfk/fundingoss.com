# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ("name", "funding_status", "maintainers", "added", "website")

admin.site.register(Project, ProjectAdmin)

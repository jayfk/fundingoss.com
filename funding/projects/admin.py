# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = (
        "name", "funding_status", "license", "added", "website"
    )
    list_editable = list_display
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)

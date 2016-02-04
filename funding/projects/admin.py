# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib import admin
from django import forms
from .models import Project


class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ()

    funding_type = forms.MultipleChoiceField(
        choices=Project.FUNDING_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    form = ProjectAdminForm
    list_display = (
        "name", "funding_status", "license", "added", "website"
    )
    list_editable = list_display
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)

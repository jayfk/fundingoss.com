# -*- coding: utf-8 -*-
from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name", "website", "languages", "function", "maintainers", "added", "needs",
            "funding_status", "funding_type", "funding_status_notes", "license"
        )

    funding_type = forms.MultipleChoiceField(
        choices=Project.FUNDING_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

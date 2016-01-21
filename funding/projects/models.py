# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):

    # this needs some more work
    STATUS_CHOICES = (
        ("well_funded", "Well Funded"),
        ("self_funded", "Self Funded"),
        ("no_funding", "No Funding"),
        ("unknown", "Unknown")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)
    website = models.URLField(max_length=100)
    languages = ArrayField(
        models.CharField(max_length=100),
        help_text="Primary Language or Community. (seperate, with, comma)"
    )
    function = models.CharField(max_length=200)
    maintainers = ArrayField(
        models.CharField(max_length=100),
        help_text="Name a Maintainer (GitHub, email, Twitter etc. seperate, with, comma)"
    )
    added = models.CharField(max_length=100,
                             help_text="Who Added This (your GitHub, email, Twitter, etc)")
    needs = models.TextField(blank=True,
                             help_text="Add'l Notes on Project Needs (1 sentence or less)")
    funding_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    funding_status_notes = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)

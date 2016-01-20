# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):

    STATUS_CHOICES = (
        ("well_funded", "Well Funded"),
        ("self_funded", "Self Funded"),
        ("no_funding", "No Funding"),
        ("unknown", "Unknown")
    )

    name = models.CharField(max_length=50, unique=True)
    website = models.URLField(max_length=100)
    languages = ArrayField(
        models.CharField(max_length=100)
    )
    function = models.CharField(max_length=200)
    maintainers = ArrayField(
        models.CharField(max_length=100)
    )
    added = models.CharField(max_length=100)
    needs = models.TextField(blank=True)
    funding_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    funding_status_notes = models.TextField(blank=True)

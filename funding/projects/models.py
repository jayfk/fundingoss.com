# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Project(models.Model):

    STATUS_CHOICES = (
        ("well_funded", "Well Funded"),
        ("somewhat_funded", "Somewhat funded"),
        ("no_funding", "No Funding"),
        ("unknown", "Unknown")
    )

    FUNDING_TYPE_CHOICES = (
        ("corporate", "Corporate"),
        ("individual", "Individual"),
        ("foundation", "Foundation"),
        ("academia", "Academia"),
        ("consulting_services", "Consulting/Services"),
    )

    LICENSE_CHOICES = (
        ("apache_2", "Apache 2.0"),
        ("bsd_3", "BSD 3-Clause (New)"),
        ("bsd_2", "BSD 2-Clause (FreeBSD)"),
        ("gpl", "GPL"),
        ("lgpl", "LGPL"),
        ("mit", "MIT"),
        ("mpl", "Mozilla Public License 2.0"),
        ("epl", "Eclipse Public License"),
        ("unknown", "Unknown"),
        ("other", "Other")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)
    website = models.URLField(max_length=100)
    languages = ArrayField(
        models.CharField(max_length=100),
        help_text="Primary Language or Community. (seperate, with, comma)"
    )
    function = models.TextField(blank=True)
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
    funding_type = ArrayField(
        models.CharField(max_length=30, choices=FUNDING_TYPE_CHOICES),
        help_text="Where do you receive funding from? (Leave empty if no funding)",
        blank=True,
        default=[]
    )
    license = models.CharField(max_length=20, choices=LICENSE_CHOICES, default="unknown")

    class Meta:
        ordering = ("name",)

    def displayable_funding_types(self):
        type_map = dict(self.FUNDING_TYPE_CHOICES)
        for item in self.funding_type:
            yield type_map[item]

# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from ..models import Project
register = template.Library()

@register.simple_tag(name="status_label")
def status_label(status):
    css_map = {
        "well_funded": "success",
        "self_funded": "warning",
        "no_funding":  "danger",
        "unknown": "default"
    }

    return mark_safe("<span class='label label-{css_class} pull-xs-right'>{status}</span>".format(
        css_class=css_map.get(status, "default"),
        status=dict(Project.STATUS_CHOICES).get(status, "unknown")
    ))

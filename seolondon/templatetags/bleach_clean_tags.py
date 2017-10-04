# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from bleach import clean

register = template.Library()


@register.filter
@stringfilter
def bleach_simple_clean(string_input):
    return clean(string_input, tags=[], strip=True)

# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def aws_static_url(file_name):
    return '{}{}'.format(
        settings.AWS_STATIC_URL, file_name.lstrip('/'))

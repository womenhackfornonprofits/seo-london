# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from seo_post.models import PostCategory, Post

register = template.Library()


@register.assignment_tag
def get_post_categories():
    return PostCategory.objects.all()


@register.assignment_tag
def get_post_types():
    return list(map(lambda x: x[0], Post.POST_TYPES))


@register.filter
def get_header_color(post_type):
    if post_type == 'news':
        return 'orange'
    elif post_type == 'blog':
        return 'red'
    return 'blue'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import namedtuple
from django import template

register = template.Library()


SocialShareConfig = namedtuple(
    'SocialShareConfig',
    ['slug', 'name', 'url', 'icon']
)

_social_share_configs = [
    SocialShareConfig(
        'facebook',
        'Facebook',
        'https://www.facebook.com/sharer.php?u={url}',
        'circular inverted facebook f icon'
    ),
    SocialShareConfig(
        'twitter',
        'Twitter',
        'https://twitter.com/intent/tweet?url={url}&text={title}',
        'circular inverted twitter icon'
    ),
    SocialShareConfig(
        'linkedin',
        'Linkedin',
        'https://www.linkedin.com/shareArticle?url={url}&title={title}',
        'circular inverted linkedin icon'
    ),
    SocialShareConfig(
        'gplus',
        'Google Plus',
        'https://plus.google.com/share?url={url}',
        'inverted circular google plus icon'
    ),
]


@register.inclusion_tag('seolondon/templatetags/social_sharing.html')
def social_sharing(url, title, extra_icon_css=''):
    social_sharings = []
    for social_share_config in _social_share_configs:
        share_data = social_share_config._asdict()
        share_data['url'] = share_data['url'].format(url=url, title=title)
        social_sharings.append(share_data)
    return {
        'social_sharings': social_sharings,
        'extra_icon_css': extra_icon_css
    }

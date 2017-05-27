# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from seolondon.settings.includes.base import env


GOOGLE_ANALYTICS_TRACKING_ID = env.str(
    'GOOGLE_ANALYTICS_TRACKING_ID', default=''
)
GOOGLE_GTM_CONTAINER_ID = env.str('GOOGLE_GTM_CONTAINER_ID', default='')

CONSTANT_CONTACT_CA_ID = env.str('CONSTANT_CONTACT_CA_ID', default='')
CONSTANT_CONTACT_DEFAULT_LIST_ID = env.str(
    'CONSTANT_CONTACT_DEFAULT_LIST_ID', default='')
CONSTANT_CONTACT_ALUMNI_LIST_ID = env.str(
    'CONSTANT_CONTACT_ALUMNI_LIST_ID',
    default=CONSTANT_CONTACT_DEFAULT_LIST_ID)

IFRAMELY_API_KEY = env.str('IFRAMELY_API_KEY', default='')

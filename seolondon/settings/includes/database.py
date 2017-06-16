# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from seolondon.settings.includes.base import env


DATABASES = {
    'default': env.db(
        default='postgres://seolondon:seolondon@localhost:5432/seolondon'
    )
}

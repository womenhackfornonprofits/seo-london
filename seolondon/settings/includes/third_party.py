# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from seolondon.settings.includes.external import IFRAMELY_API_KEY


CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_DATABASE_PREFIX = 'constance:seolondon:'

CONSTANCE_CONFIG = OrderedDict([
    ('APPLY_TO_SEO_LINK',
     ('https://goo.gl/forms/eLwmi1IqRUbWZ05t2', 'APPLY TO SEO LINK', 'url')),
])

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': ('APPLY_TO_SEO_LINK',),
}

CONSTANCE_ADDITIONAL_FIELDS = {
    'url': ['django.forms.fields.URLField'],
}


CKEDITOR_CONFIGS = {
    'seopost_ckeditor': {

        'extraPlugins': 'filerimage,preview,embed',
        'removePlugins': 'image',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['Format', 'Styles'],
            [
                'Bold', 'Italic', 'Underline',
                '-', 'Link', 'Unlink', 'Anchor',
                '-', 'RemoveFormat',
            ],
            ['FilerImage'],
            [
                'HorizontalRule',
                '-', 'Table',
                '-', 'BulletedList', 'NumberedList',
                '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
            ],
            ['Preview', 'Embed', 'ShowBlocks', 'Source']
        ]
    },
}

if IFRAMELY_API_KEY:
    CKEDITOR_CONFIGS['seopost_ckeditor'].update({
        'embed_provider': (
            '//iframe.ly/api/oembed?url={{url}}&'
            'callback={{callback}}&api_key={api_key}'.format(
                api_key=IFRAMELY_API_KEY
            ))
        })

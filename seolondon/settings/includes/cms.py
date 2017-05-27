# -*- coding: utf-8 -*-
from __future__ import unicode_literals

CMS_MAX_PAGE_PUBLISH_REVERSIONS = 5

CMS_LANGUAGES = {
    1: [
        {
            'hide_untranslated': False,
            'code': 'en',
            'redirect_on_fallback': True,
            'public': True,
            'name': 'en',
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('homepage.html', 'Homepage'),
    ('careers.html', 'Careers Landing Page'),
    ('careers-inner.html', 'Careers Inner Page'),
    ('careers-inner-corporates.html', 'Careers Inner (Corporates) Page'),
    ('careers-inner-civil.html', 'Careers Inner (Civil Service) Page'),
    ('scholars.html', 'Scholars Page'),
    ('about.html', 'About Page'),
    ('get-involved.html', 'Get Involved Page'),
    ('success-stories.html', 'Success Stories Page'),
    ('who-we-support.html', 'Who We Support Page'),
    ('connect.html', 'Connect Page'),
    ('plain.html', 'Plain Page'),
    ('faq.html', 'FAQ Page'),
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    '': {'TextHolder'}
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

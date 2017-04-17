# -*- coding: utf-8 -*-

from django.conf import settings


def google_tracking(request):

    context = {}
    if getattr(settings, 'GOOGLE_GTM_CONTAINER_ID', ''):
        context['GOOGLE_GTM_CONTAINER_ID'] = \
            settings.GOOGLE_GTM_CONTAINER_ID
    elif getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_ID', ''):
        context['GOOGLE_ANALYTICS_TRACKING_ID'] = \
            settings.GOOGLE_ANALYTICS_TRACKING_ID

    return context


def constant_email(request):

    context = {}
    if getattr(settings, 'CONSTANT_CONTACT_CA_ID', ''):
        context['CONSTANT_CONTACT_CA_ID'] = \
            settings.CONSTANT_CONTACT_CA_ID
    if getattr(settings, 'CONSTANT_CONTACT_DEFAULT_LIST_ID', ''):
        context['CONSTANT_CONTACT_DEFAULT_LIST_ID'] = \
            settings.CONSTANT_CONTACT_DEFAULT_LIST_ID
    if getattr(settings, 'CONSTANT_CONTACT_ALUMNI_LIST_ID', ''):
        context['CONSTANT_CONTACT_ALUMNI_LIST_ID'] = \
            settings.CONSTANT_CONTACT_ALUMNI_LIST_ID
    return context

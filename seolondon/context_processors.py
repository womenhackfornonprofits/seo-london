# -*- coding: utf-8 -*-

from django.conf import settings

def google_analytics(request):
    return {
       'GOOGLE_ANALYTICS_TRACKING_CODE':
           getattr(settings,
		   'GOOGLE_ANALYTICS_TRACKING_CODE', '')
    }

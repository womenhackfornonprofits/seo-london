# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from seo_job.cms_menus import SeoJobMenu


class SeoJobApphook(CMSApp):
    app_name = "seo_job"
    name = _("SEO Jobboard Application")
    urls = ["seo_job.urls"]
    menus = [SeoJobMenu]


apphook_pool.register(SeoJobApphook)  # register the application

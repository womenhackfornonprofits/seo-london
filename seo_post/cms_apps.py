# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SeoPostApphook(CMSApp):
    app_name = "seo_post"
    name = _("SEO Blog/News Application")
    urls = ["seo_post.urls"]


apphook_pool.register(SeoPostApphook)  # register the application

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class SeoPostMenu(CMSAttachMenu):
    name = _("post menu")

    def get_nodes(self, request):
        nodes = []
        nodes.append(NavigationNode(
            _('Blog'),
            reverse('seo_post:post_list_by_type',
                    kwargs={'post_type': 'blog'}),
            1
        ))
        nodes.append(NavigationNode(
            _('News'),
            reverse('seo_post:post_list_by_type',
                    kwargs={'post_type': 'news'}),
            2
        ))
        return nodes

menu_pool.register_menu(SeoPostMenu)

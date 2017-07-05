# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.toolbar.items import Break


@toolbar_pool.register
class PostToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, _('Site'))
        position = admin_menu.find_first(
            Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu(
            'post-menu', _('Connect'), position=position)
        url = reverse('admin:seo_post_post_changelist')
        menu.add_link_item(_('Jobs Board'), url=url)
        admin_menu.add_break('post-break', position=menu)

        menu.add_modal_item(
            name=_('Add new Job'),
            url=reverse('admin:seo_post_post_add'),
        )

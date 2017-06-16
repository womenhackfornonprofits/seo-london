# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PlainText


class PlainTextPlugin(CMSPluginBase):
    model = PlainText
    name = _('Plain Text')
    render_template = 'djangocms_plain_text/text.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(PlainTextPlugin)

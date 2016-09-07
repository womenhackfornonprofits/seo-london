# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class PlainText(CMSPlugin):
    """
    A plain text plugin
    """
    plain_text = models.TextField(_('Plain Text'))

    def __str__(self):
        return self.plain_text[:64]

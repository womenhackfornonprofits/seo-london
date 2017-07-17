# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet, Q
from django.utils import timezone


class JobQuerySet(QuerySet):

    def published(self):
        return self.filter(
            Q(date_expire__isnull=True) |
            Q(date_expire__gte=timezone.now()),
            date_publish__lte=timezone.now(),
            is_public=True
        )

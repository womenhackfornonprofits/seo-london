# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from ckeditor.fields import RichTextField

from seo_job.querysets import JobQuerySet


@python_2_unicode_compatible
class Job(models.Model):

    job_title = models.CharField(
        max_length=100
    )

    company_name = models.CharField(
        max_length=50
    )

    location = models.CharField(
        max_length=50
    )

    min_salary = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9,
        decimal_places=2
    )

    max_salary = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9,
        decimal_places=2
    )

    job_detail = RichTextField(
        blank=True,
        config_name='seojob_ckeditor'
    )
    summary = models.TextField()

    external_url = models.URLField(blank=True)

    apply_url = models.URLField(blank=True)

    is_public = models.BooleanField(default=False)

    date_publish = models.DateTimeField(
        default=timezone.datetime.now
    )
    date_expire = models.DateTimeField(
        null=True,
        blank=True
    )
    date_updated = models.DateTimeField()

    objects = JobQuerySet.as_manager()

    # TODO: add view counts somewhere

    def __str__(self):
        return '{} {}'.format(
            self.job_title,
            self.company_name
        )

    def save(self, *args, **kwargs):
        self.date_updated = timezone.datetime.now()
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'seo_job:job_detail',
            kwargs={'pk': self.pk}
        )

    def listing_url(self):
        if self.external_url:
            return self.external_url
        else:
            return self.get_absolute_url()

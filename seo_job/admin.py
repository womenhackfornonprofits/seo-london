# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf.urls import url
from django.contrib import admin
from django import forms
from django.views import generic
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from seo_job import models


_job_preview_view = generic.DetailView.as_view(model=models.Job)


class JobAdminForm(forms.ModelForm):

    summary = forms.CharField(
        required=False, max_length=300,
        widget=forms.Textarea(attrs={'rows': 3}),
    )

    def clean(self):
        cleaned_data = super(JobAdminForm, self).clean()
        external_url = cleaned_data.get("external_url")
        job_detail = cleaned_data.get("job_detail")

        if not external_url and not job_detail:
            raise forms.ValidationError(
                'Need to either populate "external url" or "job detail"'
            )

    class Meta:
        model = models.Job
        fields = '__all__'
        help_texts = {
            'is_public': (
                'Set this if it is ready to be shown to the public'
            ),
            'summary': (
                'summary of the job, shown in the list'
            ),
            'job_detail': (
                'Detail of the Job, shown in own page'
            ),
        }


@admin.register(models.Job)
class JobAdmin(PlaceholderAdminMixin, admin.ModelAdmin):

    form = JobAdminForm

    list_display = (
        'job_title', 'company_name', 'is_public', 'date_publish',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('job_title', 'is_public'),
                ('company_name', 'location'),
                ('min_salary', 'max_salary'),
                'summary',
            )
        }),
        ('Detail', {
            'fields': (
                'external_url',  'apply_url', 'job_detail',
            ),
        }),
        ('Basic Options', {
            'classes': ('collapse',),
            'fields': (
                ('date_publish', 'date_expire',)
            ),
        }),
    )

    ordering = ('-date_publish',)

    def get_urls(self):
        urls = super(JobAdmin, self).get_urls()
        my_urls = [
            url(r'^preview/(?P<pk>\d+)$',
                self.admin_site.admin_view(
                    _job_preview_view), name='preview_job'
                ),
        ]
        return my_urls + urls

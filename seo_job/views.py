# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.views import FilterView

from django.views import generic
from seo_job.models import Job
from seo_job.filters import JobBaseFilter, JobFormFilter


class JobList(FilterView):

    model = Job
    paginate_by = 14
    filterset_class = JobBaseFilter
    template_name = 'seo_job/job_list.html'

    def get_queryset(self):
        qs = super(JobList, self).get_queryset()
        return qs.published().order_by('-date_publish')

    def get_context_data(self, **kwargs):
        filter_ = kwargs.get('filter', None)
        context = {}
        qs = self.get_queryset()
        if filter_ is not None:
            form_filter = JobFormFilter(
                data=getattr(
                    filter_.form, 'cleaned_data', {}
                ),
                queryset=qs
            )
            context = {
                'form_filter': form_filter
            }
        context.update(kwargs)
        return super(JobList, self).get_context_data(**context)


class JobDetail(generic.DetailView):

    model = Job

    def get_queryset(self):
        qs = super(JobDetail, self).get_queryset()
        return qs.published()

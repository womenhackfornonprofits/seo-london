# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views import generic
from seo_job.models import Job


class JobList(generic.ListView):

    model = Job
    paginate_by = 14

    def get_queryset(self):
        qs = super(JobList, self).get_queryset()
        return qs.published().order_by('-date_publish')

    def get_context_data(self, **kwargs):
        return super(JobList, self).get_context_data(**kwargs)


class JobDetail(generic.DetailView):

    model = Job

    def get_queryset(self):
        qs = super(JobDetail, self).get_queryset()
        return qs.published()

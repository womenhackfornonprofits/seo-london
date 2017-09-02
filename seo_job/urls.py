# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from seo_job.views import JobList, JobDetail


app_name = 'seo_job'
urlpatterns = [
    url(r'^$', JobList.as_view(), name='job_list'),
    url(r'^(?P<pk>\d+)/$',
        JobDetail.as_view(), name='job_detail')
]

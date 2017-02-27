# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from seo_post.views import PostList, PostDetail


app_name = 'seo_post'
urlpatterns = [
    url(r'^category/(?P<category>[\w-]+)/$', PostList.as_view(),
        name='post_list_by_category'),
    url(r'^(?P<post_type>[\w-]+)/$', PostList.as_view(),
        name='post_list_by_type'),
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<post_type>[\w-]+)/(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='post_detail')
]

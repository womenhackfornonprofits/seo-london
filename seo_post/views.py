# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views import generic
from seo_post.models import Post


class PostList(generic.ListView):

    model = Post

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        if 'post_type' in self.kwargs:
            qs = qs.filter(post_type=self.kwargs['post_type'])
        if 'category' in self.kwargs:
            qs = qs.filter(categories__slug=self.kwargs['category'])
        return qs.published()


class PostDetail(generic.DetailView):

    model = Post

    def get_queryset(self):
        qs = super(PostDetail, self).get_queryset()
        return qs.published()

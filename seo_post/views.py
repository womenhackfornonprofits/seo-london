# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views import generic
from seo_post.models import Post


class PostList(generic.ListView):

    model = Post
    post_type = None
    category_slug = None

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        if self.post_type:
            qs = qs.filter(post_type=self.post_type)
        if self.category_slug:
            qs = qs.filter(categories__slug=self.category_slug)
        return qs


class PostDetail(generic.DetailView):

    model = Post

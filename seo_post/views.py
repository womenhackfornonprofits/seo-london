# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views import generic
from seo_post.models import Post, PostCategory


class PostList(generic.ListView):

    model = Post
    paginate_by = 14

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        if 'post_type' in self.kwargs:
            qs = qs.filter(post_type=self.kwargs['post_type'])
        if 'category' in self.kwargs:
            qs = qs.filter(categories__slug=self.kwargs['category_slug'])
        return qs.published().order_by('-date_publish')

    def get_context_data(self, **kwargs):
        if self.kwargs.get('category_slug', None):
            kwargs['category'] = \
                PostCategory.objects.filter(
                    slug=self.kwargs['category_slug']
                ).first()
        return super(PostList, self).get_context_data(**kwargs)


class PostDetail(generic.DetailView):

    model = Post

    def get_queryset(self):
        qs = super(PostDetail, self).get_queryset()
        return qs.published()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf.urls import url
from django.contrib import admin
from django import forms
from django.views import generic
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from seo_post import models


@admin.register(models.PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


_post_preview_view = generic.DetailView.as_view(model=models.Post)


class PostAdminForm(forms.ModelForm):

    excerpt = forms.CharField(
        required=False, max_length=300,
        widget=forms.Textarea(attrs={'rows': 3}),
    )

    class Meta:
        model = models.Post
        fields = '__all__'


@admin.register(models.Post)
class PostAdmin(PlaceholderAdminMixin, admin.ModelAdmin):

    form = PostAdminForm

    list_display = ('title', 'date_publish', 'author')

    fieldsets = (
        (None, {
            'fields': ('post_type', 'title', 'body', 'is_public')
        }),
        ('Basic Options', {
            'fields': (
                'main_image', 'listing_image', 'author', 'author_image',
                'subtitle', 'excerpt',
                'date_publish', 'date_expire', 'categories',
            ),
        }),
        ('Advance Options', {
            'classes': ('collapse',),
            'fields': ('slug', ),
        }),
    )

    prepopulated_fields = {"slug": ("title",)}

    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        my_urls = [
            url(r'^preview/(?P<pk>\d+)$',
                self.admin_site.admin_view(
                    _post_preview_view), name='preview_post'
                ),
        ]
        return my_urls + urls

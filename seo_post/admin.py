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
        help_texts = {
            'author_image': (
                '"author image" is only used for Blogs entries'
            ),
            'is_public': (
                'Set this if it is ready to be shown to the public'
            ),
            'listing_image': (
                'Set this for images to be shown in '
                'news articles in the listing.  If not set, '
                '"main_image" will be used'
            ),
            'main_image': (
                'Image to be shown in the main article.  '
                'Also used as fallback for news article listing image,'
                'if listing_image is not set '
            ),
            'excerpt': (
                'summary of the article to be displayed in the listing. '
                'If not set, "body" will be shown instead'
            ),
        }


@admin.register(models.Post)
class PostAdmin(PlaceholderAdminMixin, admin.ModelAdmin):

    form = PostAdminForm

    list_display = (
        'title', 'post_type', 'is_public', 'date_publish',
    )

    fieldsets = (
        (None, {
            'fields': (
                'post_type', 'title', 'body', 'is_public', 'author'
            )
        }),
        ('Images', {
            'fields': (
                'main_image', 'listing_image', 'author_image',
            )
        }),
        ('Additional Text', {
            'fields': (
                'subtitle', 'excerpt',
            ),
        }),
        ('Basic Options', {
            'classes': ('collapse',),
            'fields': (
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from seo_post import models


@admin.register(models.PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Post)
class PostAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'date_publish', 'author')

    fieldsets = (
        (None, {
            'fields': ('post_type', 'title', 'body', 'is_public')
        }),
        ('Basic Options', {
            'fields': (
                'hero_image', 'author', 'author_image', 'excerpt',
                'date_publish', 'date_expire', 'categories',
            ),
        }),
        ('Advance Options', {
            'classes': ('collapse',),
            'fields': ('slug', ),
        }),
    )

    prepopulated_fields = {"slug": ("title",)}

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user.id
        return form

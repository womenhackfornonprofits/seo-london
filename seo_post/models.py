# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify

from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from seo_post.querysets import PostQuerySet


@python_2_unicode_compatible
class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Post(models.Model):

    BLOG = 'blog'
    NEWS = 'news'
    POST_TYPES = ((BLOG, 'Blog'), (NEWS, 'News'))

    post_type = models.CharField(max_length=20, choices=POST_TYPES)

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    date_publish = models.DateTimeField(default=timezone.datetime.now)
    date_expire = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True,
                                        related_name='blogs')
    body = HTMLField(configuration='CKEDITOR_CONFIGS_SEOPOST')
    hero_image = FilerImageField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET_NULL, null=True)

    objects = PostQuerySet.as_manager()

    # TODO: add view counts somewhere

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'seo_post:post_detail', kwargs={'slug':self.slug}
        )

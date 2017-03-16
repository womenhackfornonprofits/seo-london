# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_type', models.CharField(max_length=20, choices=[('blog', 'Blog'), ('news', 'News')])),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now)),
                ('date_expire', models.DateTimeField(null=True, blank=True)),
                ('body', ckeditor.fields.RichTextField(config_name='seopost_ckeditor')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='seo_post.Category', blank=True)),
                ('hero_image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
        ),
    ]

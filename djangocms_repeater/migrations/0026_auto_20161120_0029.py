# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0025_auto_20161120_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='storyImage',
        ),
        migrations.RemoveField(
            model_name='career',
            name='storyImage',
        ),
        migrations.RemoveField(
            model_name='multiplesingleheader',
            name='storyImage',
        ),
        migrations.RemoveField(
            model_name='singleheader',
            name='storyImage',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='storyImage',
        ),
        migrations.AddField(
            model_name='boardmember',
            name='image',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
        migrations.AddField(
            model_name='career',
            name='URL',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
        migrations.AddField(
            model_name='multiplesingleheader',
            name='backgroundImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
        migrations.AddField(
            model_name='singleheader',
            name='backgroundImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', blank=b'True'),
        ),
    ]

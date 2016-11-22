# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0024_auto_20161112_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='image',
        ),
        migrations.RemoveField(
            model_name='career',
            name='URL',
        ),
        migrations.RemoveField(
            model_name='multiplesingleheader',
            name='backgroundImage',
        ),
        migrations.RemoveField(
            model_name='singleheader',
            name='backgroundImage',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='image',
        ),
        migrations.AddField(
            model_name='boardmember',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
        migrations.AddField(
            model_name='career',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
        migrations.AddField(
            model_name='multiplesingleheader',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
        migrations.AddField(
            model_name='singleheader',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png'),
        ),
    ]

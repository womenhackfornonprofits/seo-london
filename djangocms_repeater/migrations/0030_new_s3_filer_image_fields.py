# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('djangocms_repeater', '0029_auto_20161121_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplesingleheader',
            name='backgroundImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', help_text=b'legacy field', blank=True),
        ),
        migrations.AddField(
            model_name='multiplesingleheader',
            name='new_background_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='singleheader',
            name='backgroundImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', help_text=b'legacy field', blank=True),
        ),
        migrations.AddField(
            model_name='singleheader',
            name='new_background_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', help_text=b'legacy field', blank=True),
        ),
migrations.AddField(
            model_name='successstory',
            name='new_story_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', help_text=b'legacy field', blank=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='new_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
    ]

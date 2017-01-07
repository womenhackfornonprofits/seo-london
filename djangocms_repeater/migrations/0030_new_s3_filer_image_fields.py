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
        migrations.RenameField(
            model_name='multiplesingleheader',
            old_name='backgroundImage',
            new_name='background_image_url',
        ),
        migrations.AddField(
            model_name='multiplesingleheader',
            name='background_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.RenameField(
            model_name='singleheader',
            old_name='backgroundImage',
            new_name='background_image_url',
        ),
        migrations.AddField(
            model_name='singleheader',
            name='background_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),

        migrations.RenameField(
            model_name='successstory',
            old_name='storyImage',
            new_name='story_image_url',
        ),
        migrations.AddField(
            model_name='successstory',
            name='story_image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
        ),
    ]

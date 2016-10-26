# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('djangocms_repeater', '0020_career'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answerText',
        ),
        migrations.RemoveField(
            model_name='successstory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='successstory',
            name='text',
        ),
        migrations.AddField(
            model_name='successstory',
            name='storyImage',
            field=filer.fields.image.FilerImageField(null=True, related_name='story_image', to='filer.Image', blank=True),
        ),
    ]

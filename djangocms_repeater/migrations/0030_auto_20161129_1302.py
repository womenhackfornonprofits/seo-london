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
        migrations.AddField(
            model_name='successstory',
            name='image',
            field=models.ImageField(default=b'team-members/none.jpg', upload_to=b'team-members/'),
        ),
        migrations.AddField(
            model_name='successstory',
            name='storyImageUpload',
            field=filer.fields.image.FilerImageField(related_name='sucess_stories', blank=True, to='filer.Image', null=True),
        ),
    ]

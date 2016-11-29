# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0033_auto_20161129_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='storyImage',
            field=models.URLField(default=b'http://res.cloudinary.com/seo-london/image/upload/v1479601119/placeholder_aewrin.png', null=True, blank=True),
        ),
    ]

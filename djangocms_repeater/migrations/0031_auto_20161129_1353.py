# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0030_auto_20161129_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstory',
            name='image',
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImageUpload',
            field=s3direct.fields.S3DirectField(default=b'success-stories/none.jpg'),
        ),
    ]

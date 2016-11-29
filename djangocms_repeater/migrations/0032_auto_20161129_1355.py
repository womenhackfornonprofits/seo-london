# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0031_auto_20161129_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='image',
            field=models.ImageField(default=b'team-members/none.jpg', upload_to=b'team-members/'),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImageUpload',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
        ),
    ]

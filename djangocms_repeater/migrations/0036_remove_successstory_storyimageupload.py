# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0035_remove_successstory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstory',
            name='storyImageUpload',
        ),
    ]

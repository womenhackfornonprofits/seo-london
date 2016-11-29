# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0034_auto_20161129_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstory',
            name='image',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0018_auto_20161026_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplesingleheader',
            name='captionText',
            field=models.CharField(blank=True, max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='singleheader',
            name='captionText',
            field=models.CharField(blank=True, max_length=200, default=''),
        ),
    ]

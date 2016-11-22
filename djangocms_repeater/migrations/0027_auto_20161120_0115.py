# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0026_auto_20161120_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='URL',
        ),
        migrations.AddField(
            model_name='career',
            name='careerURL',
            field=models.CharField(default=b'/', max_length=100, blank=True),
        ),
    ]

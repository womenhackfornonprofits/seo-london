# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0021_auto_20161026_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='buttonURL',
            field=models.SlugField(default=b'/', max_length=100, blank=True),
        ),
    ]

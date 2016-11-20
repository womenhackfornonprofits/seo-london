# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0027_auto_20161120_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='image',
        ),
    ]

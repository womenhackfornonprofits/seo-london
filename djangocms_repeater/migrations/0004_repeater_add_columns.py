# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0003_careerstep'),
    ]

    operations = [
        migrations.AddField(
            model_name='repeater',
            name='add_columns',
            field=models.BooleanField(default=False),
        ),
    ]

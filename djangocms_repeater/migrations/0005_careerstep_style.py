# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0004_repeater_add_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerstep',
            name='style',
            field=models.CharField(default='w', choices=[('b', 'Blue'), ('o', 'Orange'), ('w', 'White')], max_length=1),
        ),
    ]

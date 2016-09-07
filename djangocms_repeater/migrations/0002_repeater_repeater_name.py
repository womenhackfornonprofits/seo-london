# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repeater',
            name='repeater_name',
            field=models.CharField(max_length=50, default='repeater'),
            preserve_default=False,
        ),
    ]

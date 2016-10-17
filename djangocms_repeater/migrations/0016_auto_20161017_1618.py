# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0015_button_specialbutton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='buttonURL',
            field=models.URLField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0014_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='specialButton',
            field=models.CharField(max_length=1, choices=[('d', 'Donate'), ('a', 'Apply Now'), ('l', 'Log in')], default='n'),
        ),
    ]

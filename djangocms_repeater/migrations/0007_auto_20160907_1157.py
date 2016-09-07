# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0006_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logoChoice',
            field=models.CharField(max_length=1, default='0', choices=[('0', 'SEO London'), ('1', 'SEO Careers'), ('2', 'SEO Scholars'), ('3', 'SEO Connect')]),
        ),
    ]

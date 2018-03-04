# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo_job', '0002_auto_20171106_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='application_route',
            field=models.CharField(blank=True, max_length=20, choices=[('direct', 'Apply Direct'), ('seo', 'Apply through SEO')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='seniority',
            field=models.CharField(blank=True, max_length=20, choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High'), ('executive', 'Executive')]),
        ),
    ]

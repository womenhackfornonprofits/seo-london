# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0005_careerstep_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('logoChoice', models.CharField(choices=[(0, 'SEO London'), (1, 'SEO Careers'), (2, 'SEO Scholars'), (3, 'SEO Connect')], max_length=1, default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

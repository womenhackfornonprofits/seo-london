# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0019_auto_20161026_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('name', models.CharField(default='Career Name', max_length=100)),
                ('URL', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

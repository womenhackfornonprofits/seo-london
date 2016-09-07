# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0002_repeater_repeater_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerStep',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin', auto_created=True)),
                ('number', models.CharField(max_length=5, default='0')),
                ('title', models.CharField(max_length=50, default='Step')),
                ('description', models.CharField(blank=True, max_length=300, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

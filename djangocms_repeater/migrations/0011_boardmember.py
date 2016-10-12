# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0010_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200, default='Name')),
                ('title', models.CharField(max_length=400, default='Job Title')),
                ('text', models.TextField(default='Description')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

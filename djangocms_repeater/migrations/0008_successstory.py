# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0007_auto_20160907_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='cms.CMSPlugin')),
                ('storyId', models.CharField(max_length=10, default='Story ID')),
                ('name', models.CharField(max_length=50, default='Candidate Name')),
                ('excerpt', models.CharField(max_length=500, default='Excerpt')),
                ('text', models.TextField(default='Story Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

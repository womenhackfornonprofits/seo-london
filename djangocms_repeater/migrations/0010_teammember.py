# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0009_successstory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', serialize=False, parent_link=True)),
                ('name', models.CharField(max_length=200, default='Name')),
                ('title', models.CharField(max_length=400, default='Job Title')),
                ('text', models.TextField(default='Description')),
                ('image', models.ImageField(upload_to='team-members/', default='team-members/none.jpg')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlainText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, to='cms.CMSPlugin', serialize=False, parent_link=True, primary_key=True)),
                ('plain_text', models.TextField(verbose_name='Plain Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

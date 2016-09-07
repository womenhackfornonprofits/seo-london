# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repeater',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', primary_key=True, serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

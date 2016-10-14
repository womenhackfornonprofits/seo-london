# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0011_boardmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, auto_created=True, serialize=False, primary_key=True)),
                ('question', models.CharField(default='Question', max_length=10000)),
                ('answer', models.TextField(default='Answer')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

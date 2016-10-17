# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0011_boardmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False)),
                ('questionText', models.CharField(max_length=10000, default='Question')),
                ('answerText', cms.models.fields.PlaceholderField(editable=False, null=True, slotname='answerText', to='cms.Placeholder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

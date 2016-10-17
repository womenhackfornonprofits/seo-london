# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0013_singleheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('buttonText', models.CharField(max_length=100, default='Button Text')),
                ('buttonURL', models.URLField()),
                ('buttonColour', models.CharField(max_length=10, default='blue', choices=[('teal', 'Teal'), ('orange', 'Orange'), ('red', 'Red'), ('blue', 'Blue')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

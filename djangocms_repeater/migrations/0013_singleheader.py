# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0012_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='cms.CMSPlugin')),
                ('quoteText', models.CharField(default='Placeholder', max_length=500)),
                ('backgroundImage', models.ImageField(default='headers/none.jpg', upload_to='headers/')),
                ('colour', models.CharField(max_length=1, default='W', choices=[('W', 'White'), ('T', 'Teal'), ('O', 'Orange'), ('R', 'Red')])),
                ('alignment', models.CharField(max_length=1, default='L', choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

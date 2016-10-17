# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0016_auto_20161017_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='cms.CMSPlugin', serialize=False)),
                ('header_name', models.CharField(default='Slider', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MultipleSingleHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='cms.CMSPlugin', serialize=False)),
                ('quoteText', models.CharField(default='Placeholder', max_length=500)),
                ('backgroundImage', models.ImageField(default='headers/none.jpg', upload_to='headers/')),
                ('colour', models.CharField(choices=[('W', 'White'), ('T', 'Teal'), ('O', 'Orange'), ('R', 'Red')], default='W', max_length=1)),
                ('alignment', models.CharField(choices=[('L', 'Left'), ('C', 'Center'), ('R', 'Right')], default='L', max_length=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='button',
            name='specialButton',
            field=models.CharField(choices=[('d', 'Donate'), ('a', 'Apply Now'), ('l', 'Log in'), ('n', 'None')], default='n', max_length=1),
        ),
    ]

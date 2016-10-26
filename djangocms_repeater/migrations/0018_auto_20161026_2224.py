# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0017_auto_20161017_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplesingleheader',
            name='captionText',
            field=models.CharField(max_length=200, default='Placeholder'),
        ),
        migrations.AddField(
            model_name='singleheader',
            name='captionText',
            field=models.CharField(max_length=200, default='Placeholder'),
        ),
        migrations.AlterField(
            model_name='multiplesingleheader',
            name='quoteText',
            field=models.CharField(max_length=150, default='Placeholder'),
        ),
        migrations.AlterField(
            model_name='singleheader',
            name='quoteText',
            field=models.CharField(max_length=150, default='Placeholder'),
        ),
    ]

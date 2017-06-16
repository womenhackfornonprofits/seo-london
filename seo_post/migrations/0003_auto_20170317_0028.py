# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo_post', '0002_auto_20170313_2122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='PostCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('seo_post', '0003_auto_20170317_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hero_image',
            new_name='main_image',
        ),
        migrations.AddField(
            model_name='post',
            name='listing_image',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True),
        ),
    ]

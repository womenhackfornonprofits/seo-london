# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('seo_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL,
                                                     blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='SEO London', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='hero_image',
            field=filer.fields.image.FilerImageField(related_name='+', on_delete=django.db.models.deletion.SET_NULL,
                                                     blank=True, to='filer.Image', null=True),
        ),
    ]

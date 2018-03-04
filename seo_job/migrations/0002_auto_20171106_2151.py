# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seo_job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_function',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='seniority',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_detail',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(),
        ),
    ]

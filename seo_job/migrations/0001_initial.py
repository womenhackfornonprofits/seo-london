# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('min_salary', models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)),
                ('max_salary', models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)),
                ('job_detail', ckeditor.fields.RichTextField()),
                ('summary', models.TextField(blank=True)),
                ('external_url', models.URLField(blank=True)),
                ('apply_url', models.URLField(blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now)),
                ('date_expire', models.DateTimeField(null=True, blank=True)),
                ('date_updated', models.DateTimeField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0023_auto_20161112_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='text',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='text',
        ),
        migrations.AddField(
            model_name='boardmember',
            name='image',
            field=models.ImageField(default=b'board-members/none.jpg', upload_to=b'board-members/'),
        ),
    ]

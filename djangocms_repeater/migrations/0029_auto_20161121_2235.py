# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('djangocms_repeater', '0028_remove_boardmember_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmember',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='BoardMember',
        ),
    ]

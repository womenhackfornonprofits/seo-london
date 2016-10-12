# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0008_successstory'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='image',
            field=models.ImageField(default='success-stories/none.jpg', upload_to='success-stories/'),
        ),
    ]

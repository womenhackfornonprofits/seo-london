# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_repeater', '0032_auto_20161129_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successstory',
            name='image',
            field=models.ImageField(default=b'team-members/none.jpg', null=True, upload_to=b'team-members/', blank=True),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='storyImageUpload',
            field=filer.fields.image.FilerImageField(related_name='sucess_stories', blank=True, to='filer.Image', null=True),
        ),
    ]

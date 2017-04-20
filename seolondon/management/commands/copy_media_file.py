# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from filer.models.filemodels import File
from filer.models.imagemodels import Image

from django.conf import settings

AWS_PROD_REGION_NAME = 'eu-west-2'
AWS_PROD_STORAGE_BUCKET_NAME = 'seo-london-web-media'


def download_and_save_file(filer_file):
    prod_url_suffix = (
        'https://s3.{region_name}.amazonaws.com/'
        '{bucket_name}/').format(
            region_name=AWS_PROD_REGION_NAME,
            bucket_name=AWS_PROD_STORAGE_BUCKET_NAME
        )
    file_name = filer_file.file.name
    url = '{}{}'.format(
        prod_url_suffix, file_name
    )
    resp = requests.get(url)
    resp.raise_for_status()
    cf = ContentFile(resp.content)
    filer_file.file.storages['public'].save(file_name, cf)
    if isinstance(filer_file, Image):
        filer_file.file.delete_thumbnails()
        filer_file.icons


def save_filer_files():
    for filer_file in File.objects.filter(is_public=True):
        print ('processing {}'.format(filer_file))
        try:
            download_and_save_file(filer_file)
        except KeyboardInterrupt:
            return
        except requests.exceptions.HTTPError as exc:
            print (exc)


class Command(BaseCommand):
    help = 'save media data in test environment'

    def handle(self, *args, **options):
        if AWS_PROD_STORAGE_BUCKET_NAME == \
                settings.AWS_STORAGE_BUCKET_NAME:
            self.stderr.write(self.style.ERROR(
                'This command should not be run on production'
            ))
            return

        if os.environ['DJANGO_SETTINGS_MODULE'] != \
                'seolondon.settings.development':
            self.stderr.write(self.style.ERROR(
                'This command should not be run only in development env'
            ))
            return
        save_filer_files()
        self.stdout.write('Update Success')

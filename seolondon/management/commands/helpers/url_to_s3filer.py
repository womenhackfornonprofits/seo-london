# -*- coding: utf-8 -*-

import requests
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from filer.models import Image, Folder
from django.conf import settings

def copy_url_to_filer(instance, url_field_name, filer_field_nane):
    url = getattr(instance, url_field_name)
    resp = requests.get(url)

    base_filename = url.rsplit('/', 1)[1]
    base_path = '__'.join(url.rsplit('/', 3)[1:])
    user = User.objects.get(username='admin')
    folder, _ = Folder.objects.get_or_create(name='cloudinary_to_s3', owner=user)

    prefix = settings.FILER_STORAGES['public']['main']['UPLOAD_TO_PREFIX']

    filename = '{0}/c2s/{1}'.format(prefix, base_path)

    image = Image.objects.filter(file=filename).first()

    if image is None:
        cf = ContentFile(resp.content)
        image = Image(
            owner=user,
            original_filename = base_filename,
            folder=folder)

        image.file = image.file.storages['public'].save(filename, cf)
        image.save()

    setattr(instance, filer_field_nane, image)

    instance.save()
    image.icons


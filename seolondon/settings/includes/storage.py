# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from seolondon.settings.includes.base import env, base_dir


# User image uploads to S3 bucket
# AWS keys
AWS_SECRET_ACCESS_KEY = env.str('SEO_AWS_SECRET_ACCESS_KEY', default='')
AWS_ACCESS_KEY_ID = env.str('SEO_AWS_ACCESS_KEY_ID', default='')
AWS_STORAGE_BUCKET_NAME = env.str('SEO_AWS_STORAGE_BUCKET_NAME',
                                  default='seo-london-images')
AWS_PRIVATE_STORAGE_BUCKET_NAME = env.str(
    'SEO_AWS_STORAGE_BUCKET_NAME',
    default=AWS_STORAGE_BUCKET_NAME
)
AWS_S3_REGION_NAME = env.str('SEO_AWS_S3_REGION_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = 'auto'

_AWS_S3_OBJECT_PARAMETERS = {
     'CacheControl': 'max-age=31536000, public',
}

# this are for 'hard coded' files stored in AWS
AWS_STATIC_URL = \
    'https://s3.{region_name}.amazonaws.com/{bucket_name}/static/'.format(
        region_name=AWS_S3_REGION_NAME,
        bucket_name=AWS_STORAGE_BUCKET_NAME
    )
AWS_STATIC_URL = env.str('SEO_AWS_STATIC_URL', AWS_STATIC_URL)

USE_AWS_STORAGE = bool(env.str('SEO_USE_AWS_STORAGE', default=''))

if all([AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID,
        AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, USE_AWS_STORAGE]):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    FILER_STORAGES = {
        'public': {
            'main': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {
                    'object_parameters': _AWS_S3_OBJECT_PARAMETERS,
                    'querystring_auth': False,

                },
                'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
                'UPLOAD_TO_PREFIX': 'filer_public',
            },
            'thumbnails': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {
                    'object_parameters': _AWS_S3_OBJECT_PARAMETERS,
                    'querystring_auth': False,

                },
            },
        },
        'private': {
            'main': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {
                    'bucket_name': AWS_PRIVATE_STORAGE_BUCKET_NAME,
                },
                'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
                'UPLOAD_TO_PREFIX': 'filer_private',
            },
            'thumbnails': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {
                    'bucket_name': AWS_PRIVATE_STORAGE_BUCKET_NAME,
                },
            },
        },
    }
else:
    MEDIA_ROOT = base_dir.path('web/media')()
    MEDIA_URL = '/media/'

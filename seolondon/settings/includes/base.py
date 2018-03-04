# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import environ
root = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
base_dir = root.path('../')
env = environ.Env(DEBUG=(bool, False),)  # set default values and casting
environ.Env.read_env()              # reading .env file


PROJECT_ROOT = root()
BASE_DIR = base_dir()

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DEBUG = True

SECRET_KEY = 'FAKEforDEV'

ROOT_URLCONF = 'seolondon.urls'

WSGI_APPLICATION = 'seolondon.wsgi.application'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATIC_URL = '/staticfiles/'
STATIC_ROOT = root.path('static')()

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root.path('seolondon/templates')()],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'constance.context_processors.config',
                'seolondon.context_processors.google_tracking',
                'seolondon.context_processors.constant_email'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    # BASE DJANGO
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    # DJANGO CMS
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    # THIRD PARTY
    'ckeditor',
    'ckeditor_filebrowser_filer',
    'django_extensions',
    'constance.backends.database',
    'reversion',
    'storages',
    # SEO SPECIFICS
    'seolondon',
    'seo_post',
    'seo_job',
    'djangocms_repeater',
    'djangocms_plain_text',
    'seolondon.constance_apps.SeoConstanceAppConfig',
]

LANGUAGES = (
    ('en', 'en'),
)

MIGRATION_MODULES = {

}

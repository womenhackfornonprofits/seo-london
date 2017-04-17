from seolondon.settings import *

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'FAKEforDEV'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'seolondon': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

AWS_STATIC_URL=\
    'https://s3.eu-west-2.amazonaws.com/seo-london-web-media/static/'

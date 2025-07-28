"""
Django settings for fisio_connect_core project - Development with PostgreSQL.
"""

from .settings import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fisio_connect',
        'USER': 'fisio_user',
        'PASSWORD': 'fisio_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configurações adicionais para desenvolvimento
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Configurações de logging para desenvolvimento
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
} 
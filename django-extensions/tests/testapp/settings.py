# -*- coding: utf-8 -*-
import os

SECRET_KEY = 'dummy'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'tests.collisions',
    'tests.testapp',
    'tests.testapp_with_no_models_file',
    'django_extensions',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MEDIA_ROOT = '/tmp/django_extensions_test_media/'

MEDIA_PATH = '/media/'

ROOT_URLCONF = 'tests.testapp.urls'

DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': TEMPLATE_DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_URL = "/static/"

SHELL_PLUS_SUBCLASSES_IMPORT_MODULES_BLACKLIST = [
    'django_extensions.db.fields.encrypted',
    'django_extensions.mongodb.fields',
    'django_extensions.mongodb.models',
    'tests.test_encrypted_fields',
    'tests.testapp.scripts.invalid_import_script',
    'setup',
]

CACHES = {
    'default': {
        'BACKEND': 'tests.test_clear_caches.DefaultCacheMock',
    },
    'other': {
        'BACKEND': 'tests.test_clear_caches.OtherCacheMock',
    },
}

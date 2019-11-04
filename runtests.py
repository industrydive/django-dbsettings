#!/usr/bin/env python
from __future__ import absolute_import

import django
from django.conf import settings
from django.core.management import call_command


INSTALLED_APPS = (
    # Required contrib apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    # Our app and it's test app.
    'dbsettings',
)

SETTINGS = {
    'INSTALLED_APPS': INSTALLED_APPS,
    'SITE_ID': 1,
    'ROOT_URLCONF': 'dbsettings.tests.test_urls',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    'MIDDLEWARE_CLASSES': (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                ],
            },
        },
    ],
}

if not settings.configured:
    settings.configure(**SETTINGS)

if django.VERSION >= (1, 7):
        django.setup()

call_command('test', 'dbsettings')

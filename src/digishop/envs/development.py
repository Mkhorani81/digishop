from .common import *

INSTALLED_APPS = [
       'daphne',
       'drf_spectacular',
] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'digishop',
        'USER': 'digishop',
        'PASSWORD': 'Mkh81@77',
        'HOST': 'db',
        'PORT': '5432',
    }
}
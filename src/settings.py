ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ifweknew.sqlite3',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'US/Eastern'
USE_TZ = True

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True


STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SECRET_KEY = 'SET THIS IN LOCAL SETTINGS!!!'

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'ifweknew',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##############################################################################
# Environment loading
from urlparse import urlparse
from os import environ

if 'DATABASE_URL' in environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}

if 'DEBUG' in environ:
    DEBUG = (environ['DEBUG'].lower() == 'true')
    TEMPLATE_DEBUG = DEBUG

if all([tw_key in environ for tw_key in
        ('TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET',
         'TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET')]):
    TWITTER_ACCESS_TOKEN = environ['TWITTER_ACCESS_TOKEN']
    TWITTER_ACCESS_TOKEN_SECRET = environ['TWITTER_ACCESS_TOKEN_SECRET']
    TWITTER_CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
    TWITTER_CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']

##############################################################################
# Local settings overrides
# ------------------------
# Override settings values by importing the local_settings.py module.

import os
LOCAL_SETTINGS_FILE = os.path.join(os.path.dirname(__file__), 'local_settings.py')
if os.path.exists(LOCAL_SETTINGS_FILE):
    # By doing this instead of import, local_settings.py can refer to
    # local variables from settings.py without circular imports.
    execfile(LOCAL_SETTINGS_FILE)

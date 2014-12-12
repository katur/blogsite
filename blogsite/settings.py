"""
Django settings for blogsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Development uses local_settings file
try:
    from local_settings import (DEBUG, DATABASES, SECRET_KEY,
                                AWS_S3_ACCESS_KEY_ID,
                                AWS_S3_SECRET_ACCESS_KEY,
                                AWS_STORAGE_BUCKET_NAME)

# Production on heroku uses environment variables $DATABASE_URL and $SECRET_KEY
except Exception as e:
    DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
    STATIC_ROOT = 'staticfiles'
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
    'taggit',
    'blog',
    'website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blogsite.urls'

WSGI_APPLICATION = 'blogsite.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# https://devcenter.heroku.com/articles/getting-started-with-django

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

# Authentication
LOGIN_URL = 'login_url'
LOGIN_REDIRECT_URL = 'home_url'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '//s3.amazonaws.com/blogsitemedia'


# AWS / Media
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # skip some complicated shit re: AWS auth

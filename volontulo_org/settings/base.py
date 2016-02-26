"""
Django settings for volontulo_org project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import yaml
from unipath import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).ancestor(3)

LOCAL_CONFIG_FILEPATH = os.path.join(
    BASE_DIR, 'local_config.yaml'
)

with open(LOCAL_CONFIG_FILEPATH, 'r') as f:
    LOCAL_CONFIG = yaml.load(f)

SECRET_KEY = LOCAL_CONFIG.get('secret_key')
if not SECRET_KEY:
    raise ImproperlyConfigured

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '.volontulo.org',
    '.volontuloapp.org',
]
if LOCAL_CONFIG.get('allowed_host'):
    ALLOWED_HOSTS.append(LOCAL_CONFIG['allowed_host'])

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'cookielaw',
    'apps.volontulo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'volontulo_org.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'volontulo_org.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': LOCAL_CONFIG['db_user'],
        'PASSWORD': LOCAL_CONFIG['db_pass'],
        'NAME': LOCAL_CONFIG['db_name'],
        'HOST': LOCAL_CONFIG['db_host'],
        'PORT': LOCAL_CONFIG['db_port'],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Email settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False


# verify if it's required for registering user
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# settings required if we want to use @login_required decorator
LOGIN_URL = 'login'
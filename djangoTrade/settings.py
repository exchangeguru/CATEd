"""
Django settings for djangoTrade project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import, unicode_literals
import os

# Celery options

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+sqlite:///result.sqlite'
CELERY_TASK_SERIALIZER = 'json'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = (('Сергей', 'achievement008@gmail.com'),)
CELERYD_MAX_TASKS_PER_CHILD = 5

# AllAuth setting
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_INDEX_TABLESPACE = 10

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1j&=q!62_%51y9!=97n=)bel8+#y+lup1bsy31d%s=sm!9q_c+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'trade',
    'user_profile',
    'django_celery_beat',
    'allauth_temp',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'monitoring',
    'django.contrib.humanize',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.windowslive',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'djangoTrade.urls'

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

WSGI_APPLICATION = 'djangoTrade.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tradenew',
        'USER': 'root',
        'PASSWORD': '123',
        'default-character-set': 'utf-8',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'Ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_URL = '/accounts/login/'

# yandex money settings
YANDEX_MONEY_CLIENT_ID = 'BDDFD147E2F62EA4827F2F28E652CEF2F5AD328D0C1575E4F0AD8E56FCADD5CF'

YANDEX_MONEY_REDIRECT_URI = 'http://78.155.218.16:8000/wallet/'

YANDEX_MONEY_CLIENT_SECRET = '211A8533870D422A3EAB307B20897DB1A76EFD1379263CFD69FEC67630EA304A4831D7813BDEC90A866ABED2C30B9F8578EFF29962B13B70187429034EA3BF59'

STATIC_ROOT = '/opt/portal_ongrid/static'
MEDIA_ROOT = '/opt/portal_ongrid/media'
MEDIA_URL = '/media/'
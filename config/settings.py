"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    ## Extra Packages ##
    'django_cleanup.apps.CleanupConfig',
    # 'admin_honeypot',
    'django_jalali',
    'jalali_date',
    'rest_framework',

    ## My Apps ##
    'User',
    'ACL',
    'utils',
    'Admin',
    'Auth',
    'Student',
    'Teacher',
    'Class',
    'Setting',
    'Slider',
    'Chat',
    'Blog',
    'Shop',
    'ReportCard',
    'Ticket',
    'ContactUs',
    'QuizBuilder',
    'Gateway',
    'Installment',
    'Sms',
    'Help',
    'Poll',

    'Index',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'QuizBuilder.middlewares.CheckQuizzesExpirationMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = None

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'Setting.context_processor.get_default_setting_variables',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# # ! ======================= Mysql =======================#
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#
#         'OPTIONS': {
#             'sql_mode': 'traditional',
#         }
#     }
# }
#
# # ! ======================= Mysql =======================#

# ! ======================= Postgres =======================#

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.mysql',
                "NAME": config('DB_NAME'),
                "USER": config('DB_USER'),
                "PASSWORD": config('DB_PASSWORD'),
                "HOST": config('DB_HOST'),
                "PORT": config('DB_PORT'),
    }
}

# ! ======================= Postgres =======================#


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

CSRF_TRUSTED_ORIGINS = ["https://qalamesaee.com", "https://www.qalamesaee.com"]

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/uploads/'

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static", "root")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/uploads/'

LOGIN_URL = config('LOGIN_URL')
LOGIN_REDIRECT_URL = config('LOGIN_URL')
AUTH_USER_MODEL = 'User.User'

## Cuatom Setting ##
PAGINATION_NUMBER = 30

# default settings
JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S , %Y/%m/%d',
    },
}

## Swagger ##
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

MERCHANT_CODE = config('MERCHANT_CODE')
EMAIL_ADDRESS = config('EMAIL_ADDRESS')
MOBILE_NUMBER = config('MERCHANT_CODE')

# SMS
SMS_USERNAME = config('SMS_USERNAME')
SMS_PASSWORD = config('SMS_PASSWORD')
SMS_FROM_NUMBER = config('SMS_FROM_NUMBER')
SMS_WEB_SERVICE_URL = config('SMS_WEB_SERVICE_URL')

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Tehran'

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '73a26e734a2bfa'
EMAIL_HOST_PASSWORD = 'bb61fa0d1508ea'
EMAIL_PORT = '2525'

if not DEBUG:
    PREPEND_WWW = True

## URL ##
if DEBUG:
    URL = 'http://127.0.0.1:8000'
else:
    URL = 'http://fiatre.ir'

"""
Django settings for pocserver project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^+%!mnsrflamqkz!)dv&7kxt%zct-^)_c41+e59nxx$#%r0z*u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['chinook-poc-api-master.herokuapp.com', 'localhost', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Cross-Origin Resource Sharing
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # Filtering related    
    'django_filters',
    # Authentication related
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework',
    'chinookapi.apps.ChinookApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # To be used for only along with SessionAuthentication
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pocserver.urls'
CORS_ALLOW_CREDENTIALS = True
#CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:9528',
    'http://localhost:5000',
    'http://vuejs-poc-ui-maheshbodas.herokuapp.com',
    'http://reactjs-poc-ui-master.herokuapp.com'
)

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

WSGI_APPLICATION = 'pocserver.wsgi.application'

DATABASES_Heroku_test = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2k08npritnqkq',
        'USER': 'mzqftkgsfbxxwd',
        'PASSWORD': '4d2034578aea24a83039579e71ca12a9f5b21392728353f1b4a265e4df42c3f7',
        'HOST': 'ec2-184-72-236-57.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


DATABASES_Local = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Madhuri#1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Only appropriate for javascript based clients that are running in the same site as the API
        # 'rest_framework.authentication.SessionAuthentication',
        # For Client Server set up or while accessing API from other website use TokenAuthentication
        'rest_framework.authentication.TokenAuthentication',         
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'PAGINATE_BY_PARAM': 'page_size',
}

if ENVIRONMENT == 'production':
    DEBUG = False
    """ SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') """

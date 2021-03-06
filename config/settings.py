"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # django allauth
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # my apps
    'users.apps.UsersConfig',
    'students.apps.StudentsConfig',
    
    # Third party apps
    'admin_honeypot',
    'django_cleanup',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # white noise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# use this for production

# DB_NAME = config('DB_NAME')
# DB_USER = config('DB_USER')
# DB_PASSWORD = config('DB_PASSWORD')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'sql_mode': 'traditional'
#         },
#         'NAME': DB_NAME, #
#         'USER': DB_USER, #
#         'PASSWORD': DB_PASSWORD, #
#         'HOST': 'localhost',
#         'PORT': 3306
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URLS = '/media/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom user conf
AUTH_USER_MODEL = 'users.User'



# cloudinary for production

# c_name = config('')
# c_secret = config('')
# c_api_key = config('')


# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': c_name,
#     'API_KEY': c_api_key,
#     'API_SECRET': c_secret,

#     'STATIC_IMAGES_EXTENSIONS': ['jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k', 'wdp', 'jxr', 'hdp', 'png', 'gif', 'webp', 'bmp', 'tif', 'tiff', 'ico'],
# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'


# Allauth django
SITE_ID = 1

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = 'students:list_students'

ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# use this is you want to recieve email via terminal
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django Email sending configuration
email = config("MY_EMAIL_ADDRESS")
password = config("MY_EMAIL_PASSWORD")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # because am using gmail
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = email
EMAIL_HOST_PASSWORD = password
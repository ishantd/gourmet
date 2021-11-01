from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, 'gourmet/.env'))

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True if os.getenv("DEBUG")=="1" or os.getenv("DEBUG") == 1 else False

ALLOWED_HOSTS = (os.getenv("ALLOWED_HOSTS")).split(",")



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'widget_tweaks',
    
    'home',
    'accounts',
    'search',
    'recipes'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gourmet.urls'

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

WSGI_APPLICATION = 'gourmet.wsgi.application'


if os.getenv("dockerv", False) == "yes":
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE"),
            "NAME": os.environ.get("SQL_DATABASE"),
            "USER": os.environ.get("SQL_USER"),
            "PASSWORD": os.environ.get("SQL_PASSWORD"),
            "HOST": os.environ.get("SQL_HOST"),
            "PORT": os.environ.get("SQL_PORT"),
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [

]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/admin/login/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST_USER = 'gourmet@bestpcprices.in'
EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_VALIDATION = False

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_SECRET")
AWS_SES_REGION_NAME = 'ap-south-1'
AWS_DEFAULT_REGION_NAME = 'ap-south-1'
AWS_SES_REGION_ENDPOINT = 'email.ap-south-1.amazonaws.com'

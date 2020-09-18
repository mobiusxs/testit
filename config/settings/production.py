from os import environ, makedirs

import dj_database_url
from dotenv import load_dotenv

from .base import *

load_dotenv(dotenv_path=BASE_DIR / '.env')

makedirs(STATIC_ROOT, exist_ok=True)

if environ.get('ADMIN_URL'):
    ADMIN_URL = environ['ADMIN_URL']

ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split()

DATABASE_URL = environ.get('DATABASE_URL', None)

# Heroku will set a DATABASE_URL config var
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(url=DATABASE_URL, conn_max_age=600)
    }
# Docker PostgreSQL image requires separate values. Use .env file
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': environ['DATABASE_NAME'],
            'USER': environ['DATABASE_USER'],
            'PASSWORD': environ['DATABASE_PASS'],
            'HOST': environ['DATABASE_HOST'],
            'PORT': environ['DATABASE_PORT'],
            'ATOMIC_REQUESTS': True
        }
    }

DEBUG = 0

SECRET_KEY = environ['SECRET_KEY']

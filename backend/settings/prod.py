""" Production Settings """

import os
import sys
from urllib.parse import urlparse
from .dev import *
import dj_database_url
import psycopg2
# urlparse.uses_netloc.append('mysql')

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

DEBUG = bool(os.getenv('DJANGO_DEBUG', True))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['cat-mash-2000.herokuapp.com']

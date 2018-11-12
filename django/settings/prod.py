from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'istkicklschonweg.at']

# !!! Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../run/db.sqlite3'),
    }
}

# !!! Email 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAIL_TIMEOUT = None
#EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_SSL_KEYFILE = ''
EMAIL_SSL_CERTFILE = ''

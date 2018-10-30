from .base import *
DEBUG = True

SECRET_KEY = 'LOCAL_SECRET_KEY!'

ALLOWED_HOSTS = ['*']
CSRF_DISABLED = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

HOSTNAME = 'localhost'
EMAIL_MOCK_SENDING = True
SMS_MOCK_SENDING = True

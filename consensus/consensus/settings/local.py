from .base import *
DEBUG = True

SECRET_KEY = '4&a2&#k)@%j7j%1#$ga0cpwe5w5tt!t@%8a45=x!ad)310+*3i'

ALLOWED_HOSTS = ['*']
CSRF_DISABLED = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS=[]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'consensus.helpers.utils.DisableCSRFOnDebug',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
]


HOSTNAME = 'localhost'
EMAIL_MOCK_SENDING = True
SMS_MOCK_SENDING = True

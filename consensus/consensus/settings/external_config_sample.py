DEBUG = False

SECRET_KEY = '<SECRET_KEY>'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'consensus',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'a',
    }
}

HOSTNAME = 'application.heteroskedastic.com'
ANYMAIL = {
    'MAILGUN_SENDER_DOMAIN': '<MAILGUN_SERVER_NAME>',
    'MAILGUN_API_KEY': '<MAILGUN_ACCESS_KEY>',
}

SENDSMS_TWILIO_ACCOUNT_SID = '<SENDSMS_TWILIO_ACCOUNT_SID>'
SENDSMS_TWILIO_AUTH_TOKEN = '<SENDSMS_TWILIO_AUTH_TOKEN>'
SMS_DEFAULT_FROM_PHONE = '<SMS_DEFAULT_FROM_PHONE>'

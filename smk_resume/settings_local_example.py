import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1l93av97t0_c*iz%j_#a=silpbq3q!-@87=+rzien1+hmjkcc1'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', ]


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Sending emeails
# https://docs.djangoproject.com/en/dev/topics/email/
# Good for development debug
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition
# See https://www.djangopackages.com/

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'south',
    'pipeline',
    'accounts',
    'guardian',
    'easy_thumbnails',
    'userena',
    'captcha',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
          'css/normalize.css',
          'css/messages.css',
          'css/main.css',
          'css/forms.css'
        ),
        'output_filename': 'assets/main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'resume': {
        'source_filenames': (
          'css/resume.css',
        ),
        'output_filename': 'assets/resume.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'accounts': {
        'source_filenames': (
          'css/accounts.css',
        ),
        'output_filename': 'assets/accounts.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

# PIPELINE_DISABLE_WRAPPER = True
PIPELINE_JS = {
    'main': {
        'source_filenames': (
            'js/jquery-1.11.0.js',
        ),
        'output_filename': 'assets/main.js',
    },
    'resume': {
        'source_filenames': (
            'js/resume.js',
        ),
        'output_filename': 'assets/resume.js',
    },
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'


AUTHENTICATION_BACKENDS = (  
    'userena.backends.UserenaAuthenticationBackend',  
    'guardian.backends.ObjectPermissionBackend',  
    'django.contrib.auth.backends.ModelBackend',  
) 


MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smk_resume.urls'

WSGI_APPLICATION = 'smk_resume.wsgi.application'


TEMPLATE_DIRS = (BASE_DIR + '/templates/', )


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

LOCALE_PATHS = (
    BASE_DIR + '/locale',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/public/static/'
STATICFILES_DIRS = (BASE_DIR + '/static/', )
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/public/media/'


# Important section!
# (re)Define Development/Production configs

from smk_resume.settings_local import *

"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/ 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w6a-837%!(+42_9u+ze0vp$l*c^%!tkevg1dgv^m3@de7c2knj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'streetview',
    'timelapse',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql', #'django.db.backends.sqlite3',
        'NAME': 'backup_geocars',#os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'tgebru',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT= '/afs/cs.stanford.edu/u/tgebru/django/staticfiles'

STATIC_DIRS = (
  #'/afs/cs.stanford.edu/u/tgebru/django/staticfiles'
  '/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/streetview/static',
)
TEMPLATE_DIRS = (
  '/afs/cs.stanford.edu/u/tgebru/django/mytemplates',
)
STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
LOGIN_REDIRECT_URL='streetview.views.index'
   


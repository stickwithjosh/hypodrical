import os
from sys import path as pythonpath


if os.environ['DEBUG'] == 'False':
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG    
else:
    DEBUG = True
    
    

# Base application directory
APP_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
))

# Update $PYTHONPATH to include apps, project, and settings directories
pythonpath.insert(1, os.path.join(APP_DIR, 'apps'))
# pythonpath.insert(2, os.path.join(APP_DIR, 'project'))
# pythonpath.insert(3, os.path.join(APP_DIR, 'project', 'settings'))



ADMINS = (
    ('Joshua Blount', 'hello@joshuablount.com'),
)

MANAGERS = ADMINS

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'dev.db',}}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(APP_DIR, 'static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = '@))y7%=j3g@th@9t@0#-vgpnc2r0q_+_8&amp;asfl@k0%!u=fg#gg'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hypodrical.urls'
WSGI_APPLICATION = 'hypodrical.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'tagging',
    'south',
    'apps.podcast',
)


import os
from sys import path as pythonpath

# Base application directory
APP_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
))


production = os.environ.get('PRODUCTION', None)
if production:
    DEBUG = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG    
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'dev.db',}}
    MEDIA_ROOT = os.path.join(APP_DIR, 'hypodrical/media')
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = (
        os.path.join(APP_DIR, 'hypodrical/static'),
    )


STATIC_ROOT = ''
STATIC_URL = '/static/'

pythonpath.insert(1, os.path.join(APP_DIR, 'apps'))

ADMINS = (
    ('Joshua Blount', 'hello@joshuablount.com'),
)

MANAGERS = ADMINS


TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

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
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'hypodrical.urls'
WSGI_APPLICATION = 'hypodrical.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(APP_DIR, 'templates'),
    APP_DIR,
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
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'storages',
    'tagging',
    'south',
    'gravatar',
    'apps.podcast',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'hypodrical.context_processors.site_processor',
)

if production:
    from memcacheify import memcacheify
    from postgresify import postgresify

    DATABASES = postgresify()
    CACHES = memcacheify()

    SECRET_KEY = os.environ.get('SECRET_KEY')

    CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

    SITE_ID = 1

    INSTALLED_APPS = list(INSTALLED_APPS) + [
        'gunicorn',
    ]

    # Storage backends
    DEFAULT_FILE_STORAGE = 'storage.MediaS3BotoStorage'
    STATICFILES_STORAGE = 'storage.StaticS3BotoStorage'
    COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # boto settings
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET')
    AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME

    # S3 URL settings
    STATIC_URL = 'http://%s/static/' % AWS_S3_CUSTOM_DOMAIN
    MEDIA_URL = 'http://%s/media/' % AWS_S3_CUSTOM_DOMAIN
    
    STATICFILES_DIRS = (
        'static',
    )
    
    AWS_S3_SECURE_URLS = False

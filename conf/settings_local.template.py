import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '....',
        'USER': '....',
        'PASSWORD': '....',
        'HOST': '....',
    }
}

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')

ADMIN_MEDIA_PREFIX = '/media/admin/'

ADMINS = []

PREPEND_WWW = False
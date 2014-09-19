from .settings_base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'django_extensions',
)
# ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('databse_name'),
        'USER': os.environ.get('database_user'),
        'PASSWORD': os.environ.get('database_password'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


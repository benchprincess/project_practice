from config.settings.base import *
from dotenv import load_dotenv
from config.settings.prod import SECRET_KEY

ENV = load_dotenv('../../envs/.env.prod')

SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV['ALLOWED_HOSTS'].split(', ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': ENV.get('POSTGREST_HOST', 'localhost'),
        'NAME': ENV.get('POSTGRES_DBNAME', 'oz_practice'),
        'USER': ENV.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': ENV.get('POSTGRES_PASSWORD', '900326'),
        'PORT': ENV.get('POSTGRES_PORT', 5432),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
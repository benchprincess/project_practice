from config.settings.base import *
from dotenv import dotenv_values

ENV = dotenv_values(BASE_DIR / 'envs/.env.local')

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = ENV.get('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

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
from config.settings.base import *
from dotenv import load_dotenv
from config.settings.prod import SECRET_KEY

ENV = load_dotenv('../../envs/.env.prod')

SECRET_KEY = ENV.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
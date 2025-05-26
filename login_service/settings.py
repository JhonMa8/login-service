import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Carga .env
load_dotenv()

# 2. Paths básicos
BASE_DIR = Path(__file__).resolve().parent.parent

# 3. Seguridad
SECRET_KEY = os.getenv('SECRET_KEY', 'cambia-esta-clave-por-una-segura')
DEBUG = True
ALLOWED_HOSTS = []

# 4. Apps instaladas
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',

    'accounts.apps.AccountsConfig',  # tu app de usuarios

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 5. Modelo de usuario custom
AUTH_USER_MODEL = 'accounts.User'

# 6. Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 7. URLs y templates
ROOT_URLCONF = 'login_service.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'accounts' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'login_service.wsgi.application'

# 8. Base de datos PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'login-service',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 9. REST Framework + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# 10. Validadores de contraseña, localización y estáticos
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Ruta donde estarán los archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static-frontend"),
]

# Para producción (cuando uses collectstatic)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CORS_ALLOW_ALL_ORIGINS = True
APP_DIRS=True
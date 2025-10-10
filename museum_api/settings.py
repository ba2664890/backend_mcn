from pathlib import Path
from decouple import config
import dj_database_url
import os
#hhh
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# Sécurité
# ------------------------
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-here')
DEBUG = config('DEBUG', default=False, cast=bool)  # Toujours False en production

# ------------------------
# Hôtes autorisés
# ------------------------
ALLOWED_HOSTS = [
    "backendmcn-production.up.railway.app",
    ".railway.app",
    "localhost",
    "127.0.0.1",
]

# CSRF (POSTs et forms sécurisés)
CSRF_TRUSTED_ORIGINS = [
    "https://backendmcn-production.up.railway.app",
    # ajoute ton frontend si différent
    "https://ton-frontend-domain.com",
]

# ------------------------
# Applications
# ------------------------
INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'artifacts',
]

# ------------------------
# Middleware
# ------------------------
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'museum_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'museum_api.wsgi.application'

# ------------------------
# Base de données
# ------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL',
            default='postgresql://postgres.fmvvphrblamrtbpnuvcm:8W845MvoO0W7Ch1@aws-1-us-east-2.pooler.supabase.com:6543/postgres'
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

# ------------------------
# Validation des mots de passe
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------
# Internationalisation
# ------------------------
LANGUAGE_CODE = 'fr'
LANGUAGES = [('fr', 'Français'), ('en', 'English'), ('wo', 'Wolof')]
MODELTRANSLATION_LANGUAGES = ('fr', 'en', 'wo')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------
# Fichiers statiques et médias
# ------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------
# REST Framework
# ------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# ------------------------
# CORS
# ------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_ALL_ORIGINS = False  # Sécurisé pour prod

# ------------------------
# Jazzmin Admin
# ------------------------
JAZZMIN_SETTINGS = {
    "site_title": "Musée National du Sénégal",
    "site_header": "Administration du Musée",
    "site_brand": "Musée National du Sénégal",
    "site_logo": "images/logo_mcn.png",
    "welcome_sign": "Bienvenue à l’espace d’administration",
    "copyright": "© Musée National du Sénégal 2025",
    "search_model": "artifacts.Artifact",
    "related_modal_active": True,
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
}

# ------------------------
# Sécurité supplémentaire
# ------------------------
SECURE_SSL_REDIRECT = True  # redirige HTTP -> HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ------------------------
# Default primary key
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

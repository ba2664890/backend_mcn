"""
Django settings for museum_api project.

Déploiement prêt pour Railway / Supabase.
"""

from pathlib import Path
from decouple import config
import dj_database_url
import os

# --------------------------
# BASE DIR
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# SECURITY
# --------------------------
SECRET_KEY = config('SECRET_KEY', default='django-insecure-secret-key')

# DEBUG False en prod
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    "backendmcn-production.up.railway.app",
    ".railway.app",
    "localhost",
    "127.0.0.1",
]
# --------------------------
# SECURITY & CORS
# --------------------------


if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_ORIGINS = [
        "https://museum-c2haz649p-cardans-projects-cb73ad15.vercel.app",
    ]

CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://museum-c2haz649p-cardans-projects-cb73ad15.vercel.app",
]
# Autoriser le cookie CSRF cross-site
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = True  # obligatoire si SameSite=None

# --------------------------
# APPLICATIONS
# --------------------------
INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',  # avant admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API & utils
    'rest_framework',
    'corsheaders',
    'django_filters',

    # Apps locales
    'artifacts',

]

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------
# URLS & WSGI
# --------------------------
ROOT_URLCONF = 'museum_api.urls'
WSGI_APPLICATION = 'museum_api.wsgi.application'

# --------------------------
# TEMPLATES
# --------------------------
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

# --------------------------
# DATABASE
# --------------------------
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

# --------------------------
# PASSWORD VALIDATION
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------
# INTERNATIONALIZATION
# --------------------------
LANGUAGE_CODE = 'fr'
LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('wo', 'Wolof'),
]

MODELTRANSLATION_LANGUAGES = ('fr', 'en', 'wo')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'fr'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------
# STATIC & MEDIA
# --------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------
# REST FRAMEWORK
# --------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}


# --------------------------
# DJANGO JAZZMIN (Admin)
# --------------------------
JAZZMIN_SETTINGS = {
    "site_title": "Musée National du Sénégal",
    "site_header": "Administration du Musée",
    "site_brand": "Musée National du Sénégal",
    "welcome_sign": "Bienvenue à l’espace d’administration",
    "copyright": "© Musée National du Sénégal 2025",
    "search_model": "artifacts.Artifact",
    "topmenu_links": [
        {"name": "Accueil", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "artifacts", "name": "Artefacts"},
    ],
    "default_icon_parents": True,
    "default_icon_children": True,
    "related_modal_active": True,
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
}

# --------------------------
# APPEND_SLASH
# --------------------------
APPEND_SLASH = True  # pour éviter 301 sur /api

# --------------------------
# DEFAULT PRIMARY KEY
# --------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

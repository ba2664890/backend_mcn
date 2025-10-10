from pathlib import Path
from decouple import config
import dj_database_url
import os

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security ---
SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    "backendmcn-production.up.railway.app",
    ".railway.app",
    "localhost",
    "127.0.0.1",
]

# --- CSRF ---
CSRF_TRUSTED_ORIGINS = [
    "https://backendmcn-production.up.railway.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# --- Installed apps ---
INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',  # Must be before admin
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

# --- Middleware ---
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

ROOT_URLCONF = 'museum_api.urls'

# --- Templates ---
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

# --- Database ---
DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL',
            default='postgresql://postgres:password@host:port/dbname'
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
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

# --- Static & Media files ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- DRF ---
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

# --- CORS ---
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ à limiter en prod si nécessaire
CORS_ALLOW_CREDENTIALS = True  # Pour les cookies / sessions

# --- Jazzmin (admin custom) ---
JAZZMIN_SETTINGS = {
    "site_title": "Musée National du Sénégal",
    "site_header": "Administration du Musée",
    "site_brand": "Musée National du Sénégal",
    "site_logo": "images/logo_mcn.png",  # mettre dans static/images/
    "welcome_sign": "Bienvenue à l’espace d’administration",
    "search_model": "artifacts.Artifact",
    "show_sidebar": True,
    "related_modal_active": True,
    "changeform_format": "horizontal_tabs",
}

# --- Modeltranslation ---
MODELTRANSLATION_TRANSLATION_FILES = ('artifacts.translation',)

# --- Default primary key ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

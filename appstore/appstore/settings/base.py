"""
Django settings for appstore project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True')
DEV_PHASE = os.environ.get('DEV_PHASE', 'local')  # stub, local, dev, val, prod.
TYCHO_MODE = os.environ.get('TYCHO_MODE', 'null' if DEV_PHASE == 'stub' else 'live')

# "TRUE" | "FALSE"
ALLOW_DJANGO_LOGIN = os.environ.get('ALLOW_DJANGO_LOGIN',
                                    "TRUE" if DEV_PHASE == "local" or DEV_PHASE == 'stub' else "FALSE")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'core',
    'middleware',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'bootstrapform'
]

SITE_ID = 4

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.filter_whitelist_middleware.AllowWhiteListedUserOnly',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
]

# Email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'bot.commonshare@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("APPSTORE_DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
DEFAULT_SUPPORT_EMAIL = os.environ.get("APPSTORE_DEFAULT_SUPPORT_EMAIL", EMAIL_HOST_USER)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.environ.get('ACCOUNT_DEFAULT_HTTP_PROTOCOL', "http")

SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = \
    {'google':
         {'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': {'access_type': 'online'}}}

ROOT_URLCONF = 'appstore.urls'

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
                'django.template.context_processors.request',
                'appstore.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'appstore.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = 'allauth.socialaccount.context_processors.socialaccount'

DB_DIR = os.environ.get('OAUTH_DB_DIR', BASE_DIR)
DB_FILE = os.environ.get('OAUTH_DB_FILE', 'DATABASE.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_DIR, DB_FILE),
    }
}

IRODS_COLLECTION = os.environ.get('IROD_COLLECTIONS', "")
IRODS_ZONE = os.environ.get('IROD_ZONE', "")
##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
# local_settings = __import__(local_settings_module, globals(), locals(), ['*'])
# for k in dir(local_settings):
#    locals()[k] = getattr(local_settings, k)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip("/"))

# PIVOT HAIL APP specific settings
INITIAL_COST_CPU = 6
INITIAL_COST_MEM = 6  # in MB

# phenotype specific settings
PHENOTYPE_REDIRECT_URL = "https://monarchinitiative.org/analyze/phenotypes"

OIDC_SESSION_MANAGEMENT_ENABLE = True
SITE_URL = 'http://localhost:8000'

LOGIN_REDIRECT_URL = '/apps/'
LOGIN_URL = '/accounts/login'
ADMIN_URL = '/admin'
LOGIN_WHITELIST_URL = '/login_whitelist/'

REST_USE_JWT = True

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]
min_django_level = 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # keep Django's default loggers
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'timestampthread': {
            'format': "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)-25.25s  ]  %(message)s",
        },
    },
    'handlers': {
        'syslog': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/system_warnings.log',
            'formatter': 'timestampthread',
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'djangoLog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/django_debug.log',
            'formatter': 'timestampthread',
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
        },
        'app_store_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/app_store.log',
            'formatter': 'timestampthread',
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {

        '': {
            'handlers': ['app_store_log', 'console'],
            'propagate': False,
            'level': 'DEBUG'
            # 'level': 'INFO',
        },
        'django': {
            'handlers': ['syslog', 'djangoLog', 'console'],
            'level': min_django_level,
            'propagate': False,

        },
        # https://docs.djangoproject.com/en/1.11/topics/logging/#django-template
        'django.template': {
            'handlers': ['syslog', 'djangoLog'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['syslog'],
            'level': 'WARNING',
            'propagate': False,
        },
        'admin': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'tycho.client': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'tycho.kube': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

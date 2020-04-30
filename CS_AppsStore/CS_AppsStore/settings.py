import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# APPLICATION_BRAND should be set to one of:
# "braini", "scidas", "catalyst", or "commonsshare"
# This sets the logos and other CSS for the main UI
# and other pages such as login/logout, etc.
APPLICATION_BRAND = "braini"

# "TRUE" | "FALSE"
ALLOW_DJANGO_LOGIN = "FALSE"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n2mb4kf5(_%_p!raq@e58ub+mws^!a+zvn4!#a1ijm(5cob_d*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'apps_core_services',
    'middleware',
    'phenotype',
    'tycho_jupyter',
    'tycho_nextflow',
    'cloudtop_imagej',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_auth',
    # 'rest_auth.registration',
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
EMAIL_HOST_USER = 'bot.commonsshare@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'bot.commonsshare@gmail.com'
DEFAULT_SUPPORT_EMAIL = 'bot.commonsshare@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/accounts/email/'

SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = \
    {'google':
         {'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': {'access_type': 'online'}}}

ROOT_URLCONF = 'CS_AppsStore.urls'

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
                'CS_AppsStore.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'CS_AppsStore.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = 'allauth.socialaccount.context_processors.socialaccount'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'DATABASE.sqlite3'),
    }
}

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

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'
ADMIN_URL = '/admin'
LOGIN_WHITELIST_URL = '/login_whitelist/'

REST_USE_JWT = True

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]

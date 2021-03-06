"""
Django settings for mytestproject project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ww*)hg4(=r4v52pg(b%f*z((j8w3#r19pnf7_qtu7acu@bl=#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'oauth2_provider',


    'rest_framework',
    'drf_yasg',

    'people'
]

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

ROOT_URLCONF = 'mytestproject.urls'

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

WSGI_APPLICATION = 'mytestproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# drf-swagger setting
# drf-yasg
from django.urls import reverse_lazy

SWAGGER_SETTINGS = {
    'LOGIN_URL': reverse_lazy('admin:login'),  # 登录链接
    'LOGOUT_URL': '/admin/logout',  # 登出链接
    'USE_SESSION_AUTH': True,  # 当为TRUE时，将显示django的登录登出按钮，最为收取“认证”方式之一
    'PERSIST_AUTH': False,  # 一直维持认证状态,将“授权”信息存储在local storage中，设置False禁用该功能
    'REFETCH_SCHEMA_WITH_AUTH': True,  # “授权”状态改变时，重新获取API schema
    'REFETCH_SCHEMA_ON_LOGOUT': True,  # 登出时，重新获取API schema

    'DEFAULT_INFO': 'mytestproject.urls.swagger_info',  # 默认的openapi.info 其标准及含义见OpenAPI-2.0标准

    'SECURITY_DEFINITIONS': {  # OpenAPI-2.0标准的全局available安全定义
        'Basic': {
            'type': 'basic'
        },
        # 'Bearer': {
        #     'type': 'apiKey',
        #     'name': 'Authorization',
        #     'in': 'header'
        # },
        # 'Query': {
        #     'type': 'apiKey',
        #     'name': 'auth',
        #     'in': 'query'
        # },
        'Oauth2': {
            "type": "oauth2",
            "authorizationUrl": "/o/authorize/",
            "flow": "implicit",
            "scopes": {
                "people:read": "read people",
                "people:write":"write people"
            }
        }

    },

}

# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'pipe_separated': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        }
    },
    'handlers': {
        'console_log': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'pipe_separated',
        },
    },
    'loggers': {
        'drf_yasg': {
            'handlers': ['console_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['console_log'],
            'level': 'INFO',
            'propagate': False,
        },
        'swagger_spec_validator': {
            'handlers': ['console_log'],
            'level': 'INFO',
            'propagate': False,
        }
    },
    'root': {
        'handlers': ['console_log'],
        'level': 'INFO',
    }
}

# oath2.0
OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': { "people:read": "read people",
                "people:write":"write people",}
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#     )
# }

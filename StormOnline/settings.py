# -*-coding:utf-8-*-
"""
Django settings for StormOnline project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
# import django
# django.setup()
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, /static.)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------register-apps---------------------------------------
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, "extra_apps"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j1g!kza1uq5cwa52*b1oq0v*vt2xz2&h*5o9r!)uj6+80va#(n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['stormsha1.pythonanywhere.com']


# Application definition
AUTHENTICATION_BACKENDS = [
    'users.views.CustomBackend',
]

# -----------------apps-----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'reversion',
    'captcha',
    'pure_pagination',
    'ueditor',
    'ckeditor',
    'ckeditor_uploader',
    'DjangoUeditor'
]
# -------------------继承model------------------------
AUTH_USER_MODEL = "users.UserProfile"


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StormOnline.urls'

# ----------------------html------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'StormOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


# -----------------------sql---------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stormsha1$stormsha',
        'USER': 'stormsha1',
        'PASSWORD': 'stormsha@sina.com',
        'HOST': 'stormsha1.mysql.pythonanywhere-services.com'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# ----------------网站语言--------------------------------------
LANGUAGE_CODE = 'zh-hans'

# ----------------时区------------------------------------------
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
# 国际时间
# USE_TZ = True
# 本地时间
USE_TZ = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# -------------------静态文件-----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# ------------第三方收发邮件---------------
EMAIL_HOST = "smtp.sina.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "stormsha@sina.com"
EMAIL_HOST_PASSWORD = "sxc123654"
EMAIL_USE_TLS = False
EMAIL_FROM = "stormsha@sina.com"


# -----------------上传图片-----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_CONFIGS = {
#     'comment_ckeditor': {
#         'toolbar': 'custom',
#         'toolbar_custom': [
#             ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
#             ["TextColor", "BGColor", 'RemoveFormat'],
#             ['NumberedList', 'BulletedList'],
#             ['Link', 'Unlink'],
#             ["Smiley", "SpecialChar", 'Blockquote'],
#         ],
#         'width': 'auto',
#         'height': '180',
#         'tabSpaces': 4,
#         'removePlugins': 'elementspath',
#         'resize_enabled': False,
#     }
# }

CKEDITOR_CONFIGS = {
    'default': {},
    'comment_ckeditor': {
        'toolbar': (
            ['div','Source','-','Save','NewPage','Preview','-','Templates'],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Link','Unlink','Anchor'],
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
            ['Styles','Format','Font','FontSize'],
            ['TextColor','BGColor'],
            ['Maximize','ShowBlocks','-','About', 'pbckcode'],
        ),
    },
'你的Ckeditor工具栏名':{
    'toolbar':(
        ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'],
        ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
        ['Styles','Format','Font','FontSize'],
    ),
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 725,
    'width': 'auto',
    'height': 180,
    'tabSpaces': 4,
    'removePlugins': 'elementspath',
    'resize_enabled': False,
    }
}
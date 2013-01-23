DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'test_app.urls'

INSTALLED_APPS = [
    'besmart_common',
    'test_app',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'besmart_common.middleware.AllowedMethodsMiddleware',
]

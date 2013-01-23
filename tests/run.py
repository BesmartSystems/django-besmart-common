# -*- coding: utf-8 -*-
import os
import sys

test_app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_app'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_app.settings'

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner


test_settings = {
    'DATABASES':{
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'ROOT_URLCONF': 'test_app.urls',
    'INSTALLED_APPS': [
        'besmart_common',
        'test_app',
    ],
    'MIDDLEWARE_CLASSES': [
        'django.middleware.common.CommonMiddleware',
        'besmart_common.middleware.AllowedMethodsMiddleware',
    ]
}


if __name__ == '__main__':
    test_args = sys.argv[1:]

    current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    sys.path.insert(0, current_path)
    sys.path.insert(0, test_app_path)

    if not settings.configured:
        settings.configure(**test_settings)

    if not test_args:
        test_args = ['test_app']
    
    runner = DjangoTestSuiteRunner(verbosity=2, interactive=True, failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)

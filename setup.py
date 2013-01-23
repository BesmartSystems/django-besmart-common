#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


package_description = open('README.rst').read() + open('CHANGES').read()


setup(
    name='django-besmart-common',
    version = u":versiontools:besmart_common:",
    description="Tiny app to configure allowed methods directly in urls",
    long_description=package_description,
    keywords='django, middleware, urlconf, restrict methods',
    author='Sultan Imanhodjaev',
    author_email='sultan.imanhodjaev@gmail.com',
    url='https://github.com/imanhodjaev/django-besmart-common.git',
    license='LGPL',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['distribute',],
    setup_requires = ['versiontools >= 1.8',],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)

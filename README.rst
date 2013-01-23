Welcome
*******

Django besmart_commons is a set of utilities which provide common functionality
so far I added AllowedMethodsMiddleware which just checks for accept_methods
key-value in url config


Installation
************

::
    pip install git+https://github.com/imanhodjaev/django-besmart-common.git


Usage
*****

* Add besmart_common to INSTALLED_APPS

::

	INSTALLED_APPS = [
	    # ...
	    "besmart_common",
	]

* Add AllowedMethodsMiddleware to MIDDLEWARE_CLASSES

::
	MIDDLEWARE_CLASSES = [
	    # ...
	    "besmart_common.middleware.AllowedMethodsMiddleware",
	]

* Configuring urls, just add kwargs={'accept_methods': ['POST', 'GET']} in your url config

:: 
    url(r'^URL/$', 'VIEW', name='VIEW_NAME', kwargs={'accept_methods': ['POST', 'GET']}),


Have fun!

# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('test_app.views',
    url(r'^test1/$', 'test_view_ok', name='test_ok'),
    url(r'^test2/$', 'test_view_bad_method', name='test_fail', kwargs={'accept_methods': ['POST', 'GET']}),
)

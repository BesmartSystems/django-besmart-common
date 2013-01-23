# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import HttpResponse


def test_view_ok(request, **kwargs):
    return HttpResponse('OK')


def test_view_bad_method(request, **kwargs):
    return HttpResponse('BAD REQUEST')

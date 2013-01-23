# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

from besmart_common.middleware import AllowedMethodsMiddleware


class TestAllowedMethodsMiddleware(TestCase):
    def setUp(self):
        self.client = Client()


    def test_url_visits(self):
        request1 = self.client.get(reverse('test_ok'))
        request2 = self.client.get(reverse('test_fail'))

        self.assertEquals(request1.status_code, 200)
        self.assertEquals(request2.status_code, 405)

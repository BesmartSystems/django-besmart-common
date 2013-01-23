# -*- encoding: utf-8 -*-
from django.http import HttpResponseNotAllowed
from django.core.urlresolvers import resolve, Resolver404


class AllowedMethodsMiddleware(object):
    """ Checks request.method against accept_methods keyword in urls """
    def process_request(self, request):
        capture = False

        try:
            resolve_match = resolve(request.path)
            accept_methods = resolve_match.kwargs.get('accept_methods', None)
        except Resolver404:
            resolve_match = False


        if resolve_match and accept_methods:
            for method in accept_methods:
                if str(request.method).lower() in method.lower():
                    capture = True

            if False is capture:
                return HttpResponseNotAllowed('Method not allowed')

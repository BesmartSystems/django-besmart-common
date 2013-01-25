# -*- encoding: utf-8 -*-
from django.http import HttpResponseNotAllowed
from django.core.urlresolvers import resolve, Resolver404
from django.db import connection
from django.conf import settings
from sys import stdout


# mapping of ansi escape sequences 
KEYWORDS = { 
    'time': '\033[1;31m[%s]\033[0m',
    'text': '\033[2;37m%s\033[0m',
    'SELECT': '\033[1;36m%s\033[0m',
    'FROM': '\033[1;33m%s\033[0m',
    'INNER': '\033[1;31;40m%s\033[0m',
    'OUTER': '\033[1;34;40m%s\033[0m',
    'JOIN': '\033[1;31;40m%s\033[0m',
    'WHERE': '\033[1;32m%s\033[0m',
    'INSERT': '\033[0;35m%s\033[0m',
    'UPDATE': '\033[1;34m%s\033[0m',
    'DISTINCT': '\033[0;32m%s\033[0m',
}


class AllowedMethodsMiddleware(object):
    ''' Checks request.method against accept_methods keyword in urls '''
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


# the middleware class 
class TerminalLoggingMiddleware:
    def process_response(self, request, response):
        if settings.DEBUG and stdout.isatty():
            for query in connection.queries :
                _sql = query['sql'] 
                _sql = [ KEYWORDS['time'] % query['time'] ] + _sql.split( ) 
                for index, item in enumerate( _sql ):
                    if KEYWORDS.has_key( item ):
                         _sql[index] = KEYWORDS[item] % item
                    else:
                         _sql[index] = KEYWORDS['text'] % item
                print u' '.join( _sql) 
        return response

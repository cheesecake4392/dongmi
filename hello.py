# -*- coding: utf-8 -*-
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=UTF-8')])
    returnvalue = '<h1>Hello, web!胡炜的测试</h1>'
    print returnvalue
    return returnvalue

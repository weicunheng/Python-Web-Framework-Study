# -*- coding: utf-8 -*-#
"""
Name:         2.wsgi_demo
Author:       weiheng
Date:         2019/11/10
Description:  None
"""
from wsgiref.simple_server import make_server


def app(environ, start_response):
    print(environ)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return ["Hello World".encode("utf-8")]


class ClassApp(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
        yield "Hello World".encode("utf-8")


if __name__ == '__main__':
    """
    app: 应用程序必须是可调用对象(实现了__call__)， 返回值必须是一个可迭代对象(实现了__iter__)
    """
    httpd = make_server("127.0.0.1", 8000, app=app)
    print("http://{}:{}".format("127.0.0.1", 8000))
    httpd.serve_forever()

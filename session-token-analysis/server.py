
#Modifed SimpleHTTPServer which returns cookies passed on the request

import SimpleHTTPServer
import logging
import time
import base64
import random

cookieHeader = None

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.cookieHeader = self.headers.get('Cookie')
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        token = base64.b64encode( str(time.time()) + str(random.randint(1, 10)))
        self.send_header('Cookie', "Test="+token)


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)


#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os 

class MessageHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.messages = []
        BaseHTTPRequestHandler.__init__(self,args,kwargs)
    
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('content-length',0))
        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # 3. Extract the "message" field from the request data.
        parsed_data = parse_qs(data)
        print(f'parsed data: {parsed_data}')
        message = '\n'.join(parsed_data.get('message',['NO MESSAGE WAS SENT']))
        self.messages.append(message)
        
        # Send the "message" field back as the response.
        self.send_response(303)
        self.wfile.write(message.encode())

    def do_GET(self):
        filename = 'Messageboard.html'
        curdir = os.path.dirname(os.path.abspath(__file__))
        fullpath = curdir + '/' + filename
        print(f'sending: {fullpath}')
        with open(fullpath) as form:
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(form.read().encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

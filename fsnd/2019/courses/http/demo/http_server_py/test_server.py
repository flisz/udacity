import http.server

class myHTTPserver(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 200 is an 'OK' response
        self.send_response(200)
        
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write("Hello, HTTP!\n".encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, myHTTPserver)
    httpd.serve_forever()

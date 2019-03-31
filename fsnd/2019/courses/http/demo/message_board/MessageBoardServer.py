from http.server import BaseHTTPRequestHandler HTTPServer

class MessageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.response(200)

        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        message = self.make_messages()

        self.wfile.write(message.encode())

    def make_messages(self)
        output = ""
        for count, message in Enumerate(self.messages):
            output += 'Message#'+str(count)+'\n'+message+'\n'
        return output 

    def do_POST(self):
        length = int(self.headers.get('Content-length',0))
        data = self.rfile.read(length).decode()

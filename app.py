from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = '''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 24px;
                    color: #333;
                    text-align: center;
                    padding-top: 50px;
                }
            </style>
        </head>
        <body>
            Hello, World!
        </body>
        </html>
        '''
        self.wfile.write(bytes(message, "utf8"))
        return

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

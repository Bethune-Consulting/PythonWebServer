# PythonWebServer
Test Project

Just for testing dev tools.
elif self.path == '/ninchi':
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(b'{"message":"Ninchi check passed"}')

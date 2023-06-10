from http.server import BaseHTTPRequestHandler
from .response import response_http
class MyHandler(BaseHTTPRequestHandler):
    routes = {
        # '/': home_view,
        # '/about': about_view,
        # '/contact': contact_view
    }

    def do_GET(self):
        if self.path in self.routes:
            handler = self.routes[self.path]
            # self.server.middleware.process_request(self)  # Pre-process request
            response = handler(self)
            # self.server.middleware.process_response(response)  # Post-process response
        else:
            # file_path = os.path.join('static', self.path[1:])
            # if os.path.isfile(file_path):
            #     self.server.middleware.process_request(self)  # Pre-process request
            #     self.serve_static_file(file_path)
            #     self.server.middleware.process_response(None)  # Post-process response
            # else:
            response_http(self,"404 Not Found")
            # self.send_response(404)
            # self.send_header('Content-type', 'text/plain')
            # self.end_headers()
            # self.wfile.write(b'404 Not Found')

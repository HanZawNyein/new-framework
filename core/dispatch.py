from http.server import BaseHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader


from .response import response_http

class MyHandler(BaseHTTPRequestHandler):
    routes = {
        # '/': home_view,
        # '/about': about_view,
        # '/contact': contact_view
    }

    def __init__(self, *args, **kwargs):
        self.template_env = Environment(loader=FileSystemLoader('templates'))
        super().__init__(*args, **kwargs)

    def render_template(self, template_name, **kwargs):
        template = self.template_env.get_template(template_name)
        return template.render(**kwargs)

    def do_GET(self):
        if self.path in self.routes:
            handler = self.routes[self.path]
            # self.server.middleware.process_request(self)  # Pre-process request
            response = handler(self)
            # self.server.middleware.process_response(response)  # Post-process response
            return response
        else:
            # file_path = os.path.join('static', self.path[1:])
            # if os.path.isfile(file_path):
            #     self.server.middleware.process_request(self)  # Pre-process request
            #     self.serve_static_file(file_path)
            #     self.server.middleware.process_response(None)  # Post-process response
            # else:
            return response_http(self,"404 Not Found",status_code=404,content_type="text/plain")

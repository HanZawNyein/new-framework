from http.server import BaseHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader

from .response import response_http


class MyHandler(BaseHTTPRequestHandler):
    routes = {}

    def __init__(self, *args, **kwargs):
        self.template_env = Environment(loader=FileSystemLoader('templates'))
        super().__init__(*args, **kwargs)

    def render_template(self, template_name, **kwargs):
        template = self.template_env.get_template(template_name)
        return template.render(**kwargs)

    def do_GET(self):
        if self.path in self.routes:
            handler = self.routes[self.path]
            response = handler(self)
            return response
        else:
            return response_http(self, "404 Not Found", status_code=404, content_type="text/plain")

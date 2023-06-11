import os
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

    def get_content_type(self, file_path):
        extension = os.path.splitext(file_path)[1]
        if extension == '.css':
            return 'text/css'
        elif extension == '.js':
            return 'application/javascript'
        elif extension == '.jpg' or extension == '.jpeg':
            return 'image/jpeg'
        elif extension == '.png':
            return 'image/png'
        else:
            return 'application/octet-stream'

    def serve_static_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            return response_http(self, content_type=self.get_content_type(file_path), message=content, status_code=200)
        except IOError:
            return response_http(self,content_type="text/plain",message="File Not Found",status_code=404)

    def do_GET(self):
        if self.path in self.routes:
            handler = self.routes[self.path]
            response = handler(self)
            return response
        else:
            file_path = os.path.join('static', self.path[1:])
            if os.path.isfile(file_path):
                return self.serve_static_file(file_path)
            else:
                return response_http(self, "404 Not Found", status_code=404, content_type="text/plain")

class Response:
    def response_http(self, request, message, content_type="text/html", status_code=200):
        request.send_response(status_code)
        request.send_header('Content-type', content_type)
        request.end_headers()
        request.wfile.write(message.encode('utf-8'))

    def render_template(self, request, template_name, **kwargs):
        content = request.render_template(template_name, posts=kwargs)
        self.response_http(request,content)


__response = Response()
response_http = __response.response_http
render_template = __response.render_template

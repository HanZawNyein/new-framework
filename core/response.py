class Response:
    def response_http(self, request, message):
        request.send_response(200)
        request.send_header('Content-type', 'text/html')
        request.end_headers()
        request.wfile.write(message.encode('utf-8'))

__response = Response()
response_http = __response.response_http
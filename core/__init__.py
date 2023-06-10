import logging

from . import server
from . import dispatch
from . import response

logging.basicConfig(level=logging.INFO)

def run(http_server,host,port,handler):
    server = http_server((host, port), handler)
    logging.info(f'Starting server on https://{host}:{port}')
    server.serve_forever()
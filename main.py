from core import run
from core.server import MyHTTPServer
from urls import Handler

if __name__ == '__main__':
    run(http_server=MyHTTPServer, host="localhost", port=8000, handler=Handler)

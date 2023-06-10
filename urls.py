from core.dispatch import MyHandler
import views


class Handler(MyHandler):
    routes = {
        "/": views.home_view
    }

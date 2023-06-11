from core.response import response_http, render_template


def home_view(request):
    data = {"hello": "a"}
    return render_template(request, "home.html", data)

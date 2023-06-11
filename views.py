from core.response import response_http, render_template


def home_view(request):
    data = [{"a": a, "b": a * 2, "c": a * 4} for a in range(100)]
    context = {"data": data}
    return render_template(request, "home.html", context)

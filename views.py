from core.response import response_http
def home_view(request):
    return response_http(request,"Hello Home")

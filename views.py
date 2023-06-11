from core.response import response_http,render_template
def home_view(request):
        posts = {"a":"a"}
        render_template(request,"home.html")
        # content = request.render_template('home.html', posts=posts)
        # request.send_response(200)
        # request.send_header('Content-type', 'text/html')
        # request.end_headers()
        # request.wfile.write(content.encode('utf-8'))

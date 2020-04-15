def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

from wsgiref.simple_server import make_server

# 创建一个服务，指定端口、处理函数
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听http请求
httpd.serve_forever()

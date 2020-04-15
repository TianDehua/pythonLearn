import socket
import threading
import time

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定网络，监听端口
s.bind(('127.0.0.1', 9999))

# 设置最大连接数
s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
while True:
    # 阻塞等待新连接
    print('server start accept-----')
    sock, addr = s.accept()
    print('server accept success-----')
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

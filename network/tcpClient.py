import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 9999))

# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))

for i in range(3):
    # 发送数据:
    str = input('请输入：')
    s.send(str.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close
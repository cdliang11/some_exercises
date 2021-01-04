from socket import *

HOST = 'www.baidu.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpClisock = socket(AF_INET, SOCK_STREAM)
tcpClisock.connect(ADDR)
tcpClisock.send(str('GET/\n').encode('utf-8'))
data = tcpClisock.recv(BUFSIZ).decode('utf-8')
with open(r"webpage.txt", 'w') as f:
    f.write(data)

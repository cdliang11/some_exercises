from socket import *

DefaultHOST = 'localhost'
DefaultPOST = 21567
BUFSIZ = 1024

# get host and port
def GetAddr():
    host = input("Please input host: ")
    port = input("Please input port: ")
    return host, port

host, port = GetAddr()

if not host:
    host = DefaultHOST
if not port:
    port = int(DefaultPOST)

ADDR = (host, port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
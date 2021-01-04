from socket import *

DefaultHOST = 'localhost'
DefaultPOST = 21567
BUFSIZ = 1024

# get host and port
def GetAddr():
    host = raw_input("Please input host: ")
    port = raw_input("Please input port: ")
    return host, int(port)

host, port = GetAddr()

if not host:
    host = DefaultHOST
if not port:
    port = DefaultPOST

ADDR = (host, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)

udpCliSock.close()
from socket import *
from time import ctime
import os
import re

HOST = ""
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
responsedic = {'date':ctime(), 'os':os.name, 'ls':str(os.listdir(os.curdir))}

while True:
    print("Waiting for connect...")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        findre = re.match(r'ls dir\((.+)\)', str(data))
        
        if not data:
            break
        elif responsedic.get(data):
            tcpCliSock.send(responsedic[data].encode('utf-8'))
        elif findre:
            print(os.listdir(findre.group(1)))
            tcpCliSock.send(str(os.listdir(findre.group(1))).encode('utf-8'))
        else:
            tcpCliSock.send(data.encode('utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
from socket import *
import threading
from time import sleep
HOST = 'localhost'
PORT = 2050
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
username = input('Please set your username: ')
tcpCliSock.send(("%s join the server" % username).encode('utf-8'))
data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
print(data)
room = input("Input room number(Input a number 1-9): ")
tcpCliSock.send(("Join the room%s" % room).encode('utf-8'))
data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
print(data)
def send():
    while True:
        data = input("> ")
        if not data:
            continue
        else:
            tcpCliSock.send(data.encode('utf-8'))

def receive():
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        print(data)
        print('> ')
try:
    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=receive)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
# except(EOFError, KeyboardInterrupt):
#     tcpCliSock.close()


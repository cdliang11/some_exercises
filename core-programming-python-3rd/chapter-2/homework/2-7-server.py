from socket import *

HOST = ""
PORT = 2051
ADDR = (HOST, PORT)
BUFSIZ = 1024
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("Waiting for connect...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connect from: ", addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        if data == 'Quit':
            tcpCliSock.close()
        else:
            print("%s said: %s" % (addr, data))
        senddata = ""
        while senddata == "":
            senddata = input('> ')
        tcpCliSock.send(senddata.encode('utf-8'))
        data = None
tcpCliSock.close()
tcpSerSock.close()
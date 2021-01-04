import socket
import select
import re

server = socket.socket()
ADDR = ("", 2050)
server.bind(ADDR)
server.listen(5)
inputs = [server]
clientdict = {}
user = "No name user"
roomnumber = 0
print("Start the chat server...")


while True:
    # select接收并监控三个通信列表 第一个监控所有外部发送的数据 第二个监控和接收所有要发出去的数据
    # 第三个监控错误信息
    
    readable, writable, exception = select.select(inputs, [], []) #
    for i in readable:
        if i == server: #判断当前触发的是不是服务端对象，当触发服务端对象的时候，是新用户连接进来
            # 表示新用户连接
            client, addr = i.accept()
            print("Connected from ", addr, "This is user %s" % user)
            inputs.append(client) # 将新用户加入到监听列表
            clientdict[client] = [client, addr, user, roomnumber]
        else:
            try:
                # 接收老用户信息
                data = i.recv(1024).decode('utf-8')
                matchname = re.match(r'(.+)\sjoin the server', data)
                matchroom = re.match(r'Join the room(\d)', data)
                if matchname:
                    print(data)
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][2] == 'No name user' or clientdict[x][3] == 0:
                                pass
                            else:
                                x.send(data.encode('utf-8'))
                                # x.close()
                    username = matchname.group(1)
                    clientdict[i][2] = username
                    i.send(('Welcome, %s' % username).encode('utf-8'))
                    # i.close()
                elif matchroom:
                    print('%s' % clientdict[i][2], data)
                    roomnumber = matchroom.group(1)
                    clientdict[i][3] = roomnumber
                    i.send(("You join room %s" %roomnumber).encode('utf-8'))
                    # i.close()
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][3] == clientdict[i][3]:
                                x.send(("%s join this room"%clientdict[i][2]).encode('utf-8'))
                                # x.close()
                else:
                    senddata = '%s said: %s' %(clientdict[i][2], data)
                    for x in inputs:
                        if x == server or x == i:
                            pass
                        else:
                            if clientdict[x][3] == clientdict[i][3]:
                                x.send(senddata.encode('utf-8'))
                                # x.close()
                disconnect = False
            
            except socket.error:
                disconnect = True
            
            if disconnect:
                leftdata = "%s has left" % clientdict[i][2]
                print(leftdata)
                for x in inputs:
                    if x == server or x == i:
                        pass
                    else:
                        x.send(leftdata.encode('utf-8'))
                        # x.close()
                inputs.remove(i)
  
                

    
    
    

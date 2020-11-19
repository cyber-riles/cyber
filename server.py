import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8096))
server.listen(5)
(client, (ip,port)) = server.accept()
data="test"
while len(data):
    data=client.recv(2048)
    print "client sent : ",data
    client.send(data)

client.close()
server.close()

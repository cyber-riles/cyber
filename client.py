import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8096))
request=raw_input("message")
client.send(request)
response=client.recv(2048)
print response

client.close()
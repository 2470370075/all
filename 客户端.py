import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
data=sk.recv(1024).decode('utf-8')
print(data.upper())
sk.send(data.upper().encode('utf-8'))
sk.close()

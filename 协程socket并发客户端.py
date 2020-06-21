import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
while 1:
    sk.send(input('>>:').encode('utf-8'))
    data=sk.recv(1024)
    print(data.decode('utf-8'))

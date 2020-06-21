import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
while 1:
    say=input('')
    sk.send(say.encode('utf-8'))
    data=sk.recv(1024).decode('utf-8')
    print(data)

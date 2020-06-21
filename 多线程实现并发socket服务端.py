import socket
import threading

def f1():

    while 1:
        data = conn.recv(1024)
        print(data)
        conn.send('ok'.encode('utf-8'))

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)
while 1:
    conn, adrr = sk.accept()
    threading.Thread(target=f1,args=()).start()


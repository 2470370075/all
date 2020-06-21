from gevent import monkey;monkey.patch_all()
import socket
import gevent

def talk():
    data = conn.recv(1024).decode('utf-8')
    print(data)
    conn.send('ok'.encode('utf-8'))




sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(5)
while 1:
    conn,_=sk.accept()

    g1=gevent.spawn(talk())


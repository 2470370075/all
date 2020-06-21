import socket
from multiprocessing import Process
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))

def recv(conn):
    data=conn.recv(1024).decode('utf-8')
    print(data)

def send(conn):
    print('开始')
    x=input('>>:').encode('utf-8')
    conn.send(x)

if __name__=='__main__':
    phone.listen(5)
    conn,adrees=phone.accept()
    p1=Process(target=send,args=(conn,))
    p1.start()







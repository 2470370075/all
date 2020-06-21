from multiprocessing import Process
import socket,struct,json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

def recv(phone):
    data=phone.recv(1024).decode('utf-8')
    print(data)

def send(phone):
    x=input('>>').encode('utf-8')
    phone.send(x)

if __name__=='__main__':
    for i in range(10):
        p1=Process(target=recv,args=(phone,))
        p1.start()










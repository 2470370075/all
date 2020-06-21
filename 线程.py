from threading import Thread
from multiprocessing import Process
import threading
import time
#
def f(n):
    print(n)

n=0

for i in range(10):
    n+=1
    p=Thread(target=f,args=(n,))
    p.start()

def f(name):                                                 # 由于全局解释器所，多线程对于计算密集的函数并没有提高效率
    global n
    n = 7 ** 7 ** 8
    print('my name is {}号'.format(name))
#
#
# import datetime
# x = datetime.datetime.now()
# l = []
# for i in range(7):
#     p1=Thread(target=f,args=('wjx',))
#     p1.start()
#     l.append(p1)
# for i in l:
#     i.join()
# y = datetime.datetime.now()
# print(y-x)
#
# x = datetime.datetime.now()
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# y = datetime.datetime.now()
# print(y-x)

# def f(name):                                                 # 但是对于io密集的，提高了效率
#     global n
#     time.sleep(4)
#     print('my name is {}号'.format(name))
#
#
# import datetime
# x = datetime.datetime.now()
# l = []
# for i in range(7):
#     p1=Thread(target=f,args=('wjx',))
#     p1.start()
#     l.append(p1)
# for i in l:
#     i.join()
# y = datetime.datetime.now()
# print(y-x)
#
# x = datetime.datetime.now()
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# f('jxw')
# y = datetime.datetime.now()
# print(y-x)


#



#
# #
# class mythread(Thread):                                           #开启线程的第二种方法
#     def __init__(self,name):
#         super(). __init__()
#         self.name=name
#
#     def run(self):
#         time.sleep(0.5)
#         print('{} say helloworld'.format(self.name))
#
# x=mythread('wjx')
# x.start()
#
#
#



# def f(name):                                                                      #线程方法
#     time.sleep(1)
#     print('线程信息:',threading.current_thread())
#
# for i in range(10):
#     p1=Thread(target=f,args=('wjx',))
#     p1.start()
#
# print('主线程信息:{}，主线程id:{}'.format(threading.current_thread(),threading.get_ident()))
# print(threading.enumerate())                                                #正在运行的线程列表
# print('活跃线程数:',threading.active_count())
#
# #
#
#
# def f1(name):                                        #守护线程，守护主线程结束而结束
#     time.sleep(1)
#     print('%s结束了'%(name))
#
#
# def f2(name):
#     time.sleep(5)
#     print('%s结束了'%(name))
#
# p1=Thread(target=f1,args=('wjx',))
# p1.start()
#
# p2 = Thread(target=f2, args=('jx2',))
# p2.daemon = True
# p2.start()



def f():                                             #  仍然数据不安全，需要加锁
    global n                                        # 为什么呢 不是有全局解释器锁吗
    temp=n
    # time.sleep(0.1)                                # 重点在time.sleep()上，全局解释器锁在io阻塞时释放，切换到其他线程，结果就出事了，仍然数据不安全
    n = 1 + temp
    print(n)


n=0
for i in range(10):
    p1=Thread(target=f,args=())
    p1.start()
time.sleep(1)
print(n)
#


from threading import Lock


def f():                                                    #普通锁：互斥锁
    lock.acquire()
    global n
    temp=n
    time.sleep(0.1)
    n = 1 + temp
    print(n)
    lock.release()


n=0
lock=Lock()
for i in range(10):

    p1=Thread(target=f,args=())
    p1.start()
time.sleep(2)    #等子进程完成
print(n)
#



# def f1():                                                           #死锁
#     lock1.acquire()
#     time.sleep(1)
#     lock2.acquire()
#     print('通过')
#     lock2.release()
#     lock1.release()
#
#
# def f2():
#     lock2.acquire()
#     time.sleep(1)
#     lock1.acquire()
#     print('通过')
#     lock1.release()
#     lock2.release()
#
#
# lock1=Lock()
# lock2=Lock()
#
# for i in range(4):
#
#     p1=Thread(target=f1,args=())
#     p1.start()
#
#     p2=Thread(target=f2,args=())
#     p2.start()















#
# from threading import RLock
# def f1(name):                                                           #递归锁
#     lock1.acquire()
#     time.sleep(1)
#     lock2.acquire()
#     print('{}通过'.format(name))
#     lock2.release()
#     lock1.release()
#
#
# def f2(name):
#     lock2.acquire()
#     time.sleep(1)
#     lock1.acquire()
#     print('{}通过'.format(name))
#     lock1.release()
#     lock2.release()
#
#
# lock2=lock1=RLock()
#
#
# for i in range(4):
#
#     p1=Thread(target=f1,args=('WJX',))
#     p1.start()
#
#     p2=Thread(target=f2,args=('JXW',))
#     p2.start()



# import random                                                 #事件
# from threading import  Event
# def f1(e):
#     c=0
#     while c<3:
#         e.wait(0.5)
#         if e.is_set()==True:
#             print('连接数据库')
#             break
#         else:
#             print('没连上')
#             c+=1
#     else:
#         raise TimeoutError('三次连接失败')
# def f2(e):
#     time.sleep(random.randint(0,2))
#     e.set()
#
#
# e=Event()
#
# p1=Thread(target=f1,args=(e,))
# p1.start()
# p2=Thread(target=f2,args=(e,))
# p2.start()

#
# from threading import Condition                                         #条件 多功能锁
# def f(i,):
#
#     con.acquire()
#
#     con.wait()                               #等待notify一个就过一个
#     print(i)
#     con.release()
#
#
# con=Condition()
#
# for i in range(10):
#     p=Thread(target=f,args=(i,))
#     p.start()
#
#
# while 1:
#     i=int(input())
#     con.acquire()
#     con.notify(i)                        #建钥匙
#     con.release()
#




import queue
#
# q=queue.Queue(3)                                    #先进先出
# q.put(4)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(1)                                          #get阻塞住了
#



# q=queue.LifoQueue(5)                                #后进先出
# q.put(4)
# q.put(2)
# q.put(3)
# print(q.get())


# q=queue.PriorityQueue(5)                           #优先级队列（默认以asc码排序，当队列的元素是自定义时，需要我们在元素的类中自定义出比较规则）
# q.put(4)
# q.put(5)
# q.put(3)
# print(q.get())





from concurrent.futures import ThreadPoolExecutor                              #线程池

# def f(i):
#     time.sleep(1)
#     print('{}:ok'.format(i))
#
# tpool=ThreadPoolExecutor(max_workers=5)
# for i in range(10):
#     t=tpool.submit(f,i)



#
#
from concurrent.futures import ThreadPoolExecutor                              #线程池
#
# def f(i):
#     time.sleep(1)
#     print('{}:ok'.format(i))
#     return i
#
# l=[]
# tpool=ThreadPoolExecutor(max_workers=5)         #不要超过cpu个数乘5
#
# # tpool.map(f,range(10))                       拿不到返回值
#
# for i in range(10):
#     t=tpool.submit(f,i)
#     l.append(t)
#
# tpool.shutdown()
#
#
# print([i.result() for i in l])
#
#
# print('over')


# from threading import Timer                           #定时器
# def func():
#     print('ok')
# Timer(5,func).start()
















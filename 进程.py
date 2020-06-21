from multiprocessing import Process
from multiprocessing import Lock
import json
import time


# def f():                                 # 开启进程的方法
#     while 1:
#         print('start...')
#         time.sleep(1)
#         print('end')
#
# if __name__ == '__main__':
#     p1=Process(target=f)
#     p1.start()
#






# def f(x,y):
#     while 1:
#         print(x)
#         time.sleep(1)
#         print(y)
#
# if __name__ == '__main__':
#
#     p=Process(target=f,args=('*','**'))
#     # p.daemon=True                                          # 把p设为守护进程，主程序运行完了p就停了
#     p.start()
#     # time.sleep(2.6)
#     time.sleep(3)
#     p.terminate()                                            # terminate()使进程结束，和守不守护无关
#     # time.sleep(3)
#     print('over1')
#     time.sleep(3)
#     print('over2')





#
def buy(i,lock):                                   #  进门上锁，一个人同步运行
    lock.acquire()
    with open('2.txt','r')as f:
        dic=json.load(f)

    time.sleep(0.1)
    if dic['ticket']>0:
        dic['ticket']-=1
        print('%s ok'%(i))
    else:
        print('%s no ok'%(i))
    time.sleep(0.1)
    with open('2.txt','w') as f:
        json.dump(dic,f)
    lock.release()

#
# if __name__ == '__main__':
#     lock=Lock()
#     for i in range(10):
#         p=Process(target=buy,args=(i,lock))
#         p.start()
#     time.sleep(1)
#





# dic={'ticket':1}
# with open('2.txt','w',encoding='utf-8') as f:
#     json.dump(dic,f)

#
# from multiprocessing import Semaphore                     # 多个人进门上锁
# #
# def buy(i,lock2):
#     lock2.acquire()
#     with open('2.txt','r')as f:
#         dic=json.load(f)
#
#     time.sleep(0.1)
#     if dic['ticket']>0:
#         dic['ticket']-=1
#         print('%s ok'%(i))
#     else:
#         print('%s no ok'%(i))
#     time.sleep(0.1)
#     with open('2.txt','w') as f:
#         json.dump(dic,f)
#     lock2.release()
#
#
# if __name__ == '__main__':
#     lock2=Semaphore(3)
#     for i in range(10):
#         p=Process(target=buy,args=(i,lock2))
#         p.start()
#     time.sleep(1)



#
from multiprocessing import Event                    #事件
from multiprocessing import Process
import random

# def cars(e,i):
#
#     if e.is_set()==True:
#         print('%s go'%(i))
#     else:
#         print('%s wait...'%(i))
#         e.wait()
#         print('%s go' % (i))
#
#
#
# def light(e):
#     while 1:
#         if e.is_set()==True:
#             e.clear()
#             print('\033[31mred\033[0m')
#         else:
#             e.set()
#             print('\033[32mgreed\033[0m')
#         time.sleep(5)
#
# if __name__ == '__main__':
#     e=Event()
#     e.set()                                       #True
#
#
#     ligh=Process(target=light,args=(e,))
#     ligh.start()
#     for i in range(20):
#         car=Process(target=cars,args=(e,i))
#         time.sleep(random.randint(1,3))
#         car.start()
#

# import os
#
# def car(e):
#     if e.is_set==True:
#         print('{}通过了'.format(os.getpid()))
#     else:
#         e.wait()
#         print('{}通过了'.format(os.getpid()))
#
# def light(e):
#     while 1:
#         if e.is_set()==True:
#             e.clear()
#             print('红灯')
#             time.sleep(3)
#         else:
#             e.set()
#             print('绿灯')
#             time.sleep(3)
#
#
# if __name__=='__main__':
#     e=Event()
#     e.set()
#     print(e.is_set())
#     p=Process(target=light,args=(e,))
#     p.start()
#     for i in range(10):
#         p2=Process(target=car,args=(e,))
#         p2.start()
#         time.sleep(2)

                                                              #生产者消费者模型
# import os,random
# from multiprocessing import JoinableQueue
# def consume(q):
#     while 1:
#
#         res=q.get()
#
#         if res==None:
#             break
#         print('吃>>：%s吃了%s'%(os.getpid(),res))
#         time.sleep(random.randint(2,3))
#         q.task_done()
#
#
# def produce(q,food):
#     for i in range(7):
#         f='%s生产的%s'%(os.getpid(),food)
#         q.put(f)
#         print('产>>：%s生产了%s'%(os.getpid(),food))
#         time.sleep(random.randint(1,3))
#     q.join()
#
# if __name__=='__main__':
#     q=JoinableQueue(5)
#     p1=Process(target=produce,args=(q,'包子'))
#     p1.start()
#     p2 = Process(target=produce, args=(q, '泔水'))
#     p2.start()
#     c1=Process(target=consume,args=(q,))
#     c1.daemon = True
#     c1.start()
#     c2 = Process(target=consume, args=(q,))
#     c2.daemon = True
#     c2.start()
#     p1.join()
#     p2.join()



#
from multiprocessing import Pool
# import time
# def f1(n):
#     print(n+1)
#
#
# if __name__=='__main__':
#     start=time.time()
#     pool=Pool(5)
#     pool.map(f1,range(100))
#     t1=time.time()-start
#
#     l=[]




#     start = time.time()
#     for i in range(100):
#         p=Process(target=f1,args=(i,))
#         p.start()
#         l.append(p)
#     for i in l:
#         i.join()
#     t2 = time.time() - start
#     print(t1,t2)
#


import os
#
# def f(i):
#         j=os.getpid()
#
#         print('{}start...'.format(j))
#
#         time.sleep(1)
#         print('{}end'.format(j))
#         return 1
#
# if __name__=='__main__':
#     p=Pool(5)
#     l=[]
#     for i in range(10):
#
#         res=p.apply_async(f,args=(i,))
#         l.append(res)
#
#     p.close()
#     p.join()
#
#     for i in l:
#         print(i.get())
#


#
# def func():
#     print(os.getpid(),'开始了')
#     time.sleep(1)
#     return 1
#
#
#
# if __name__=='__main__':
#     pool=Pool(5)
#     l=[]
#     for i in range(10):
#         p=pool.apply_async(func,args=())
#         l.append(p)
#     pool.close()
#     pool.join()
#     for i in l:
#         print(i.get())






#
# from concurrent.futures import ProcessPoolExecutor                              #进程池
#
# def f(i):
#     time.sleep(1)
#     print('{}:ok'.format(i))
#     return i
# if __name__ == '__main__':
#     l=[]
#     tpool=ProcessPoolExecutor(max_workers=5)
#     for i in range(10):
#         t=tpool.submit(f,i)
#         l.append(t)
#
#     tpool.shutdown()
#
#
#     print([i.result() for i in l])
#
#
#     print('over')
#

#
# from concurrent.futures import ProcessPoolExecutor
# def func():
#     print(os.getpid(),'开始了')
#     time.sleep(1)
#     return 1
#
# if __name__=='__main__':
#     pool=ProcessPoolExecutor(5)
#     l=[]
#     for i in range(10):
#         t=pool.submit(func,)
#         l.append(t)
#     pool.shutdown()

    # print([i.result() for i in l])

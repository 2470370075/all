from greenlet import greenlet
from gevent import monkey;monkey.patch_all()
import time
# def f1():
#     print('f1 start!')
#     time.sleep(1)
#     s2.switch()
#     print('f1 end')
#     s2.switch()
#
# def f2():
#     print('f2 start!')
#     time.sleep(1)
#     s1.switch()
#     print('f2 end')
#     s3.switch()
#
# def f3():
#     time.sleep(3)
#     print('aii over')
#
# s1=greenlet(f1)
# s2=greenlet(f2)
# s3=greenlet(f3)
# s1.switch()                                      #切换


import gevent
def f1():
    print('f1 start!')
    time.sleep(1)
    print('f1 end')


def f2():
    print('f2 start!')
    time.sleep(1)
    print('f2 end')


def f3():
    time.sleep(3)
    print('aii over')

s=time.time()
g1=gevent.spawn(f1)
g2=gevent.spawn(f2)
g3=gevent.spawn(f3)


g1.join()
g2.join()
g3.join()
e=time.time()
print(e-s)


#gevent.joinall([g1,g2,g3])
time.sleep(5)

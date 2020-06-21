from multiprocessing import JoinableQueue
from multiprocessing import Process
import random
import time

# def consume(q):
#     time.sleep(4)
#     while 1:
#         x=q.get()
#         print('吃了一个{}'.format(x))
#         time.sleep(random.randint(1,3))
#         q.task_done()
#     pass
#
# def produce(q):
#     ret='包子'
#     for i in range(3):
#         q.put(ret)
#         print('产了一个包子')
#         time.sleep(random.randint(1, 3))
#
#
#     q.join()
#
#
# if __name__ == '__main__':
#     q=JoinableQueue(5)
#     p=Process(target=produce,args=(q,))
#     p.start()
#     p2=Process(target=consume,args=(q,))
#     p2.daemon=True
#     p2.start()
#
#     p.join()


#
# import os
# def consume(q):
#     while 1:
#         x=q.get()
#         time.sleep(random.randint(1, 3))
#         print('{}吃了{}'.format(os.getpid(),x))
#         q.task_done()
#
# def produce(q):
#     ret='包子'
#     for i in range(5):
#         q.put(ret)
#         time.sleep(random.randint(1,3))
#         print('{}生产了一个包子'.format(os.getpid()))
#     q.join()
#
#
# if __name__=='__main__':
#     q=JoinableQueue(5)
#     p1=Process(target=consume,args=(q,))
#     p2 = Process(target=produce, args=(q,))
#     p1.daemon=True
#     p1.start()
#     p2.start()
#     p2.join()





#
# g=lambda x:x+1
# print(g(12))

# x=3
# y=2 if x>3 else 4
# print(y)


#
# l=[1,2,3]
# l2=[i*i for i in l if i > 2]
# print(l2)
#
# import copy
# l=[1,2,3,[2,3,4]]
# l1=l
# l2=l.copy()
# l3=copy.deepcopy(l)
# print(l1,l2,l3)
# l[1]='ww'
# l[3][0]='yy'
# print(l)
# print(l1,l2,l3)

#
#
# l1=[1,2,3]
# l2=[2,3,4]
# print([i for i in l2 if i not in l1])

import re
# s3 = "hello world ha ha"
# print(re.findall(r'(\w+)\s*',s3))

# x=0
# for i in range(1,101):
#     x+=i
# print(x)
#
# dic1={'a':1,'b':2}
# dic2={'c':3,'d':4}
# dic1.update({'c':3})
# print(dic1)
#
# with open ('2.txt','w',encoding='utf-8') as w:
#     w.write('wangjxing1')

# print(random.uniform(1,10))

#
# s='<div class="nam">中国</div>'
# print(re.findall(r'<div class=".*">(.*)</div>',s))
#
# s = "ajldjlajfdljfddd"
# s=set(s)
# s=list(s)
# s.sort()
# s='1'.join(s)
# print(s)

# dict1={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# list=sorted(dict1.items(),key=lambda i:i[0],reverse=False)
# print(list)
# dic2={}
# for i in list:
#
#     dic2[i[0]]=i[1]
# print(dic2)
#
# a = "not 404 found 张三 99 深圳"
# print(re.findall(r'[^a-z0-9\s]+',a))

# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l=[i for i in a if i%2==0]
# print(l)

# l1=[1,9,5,7,9]
# l2=[2,2,6,8]
# l3=l1+l2
# l1.sort()
# l3.sort()
# print(l3)

# import time
# t=time.time()
# print(t)
# t=time.strftime('%Y-%m-%d %X')
# print(t)
#
# l=[[1,2],[3,4],[5,6]]
# l2=[]
# for i in l:
#     for j in i:
#         l2.append(j)
# print(l2)

# a="张明 98分"
# print(re.sub('98','100',a))
#
# a = "  hehheh  "
# b=a.split()
# print(b)
#
# list=[0,-1,3,-10,5,9]
# list.sort()
# print(list)
# l2=sorted(list)
# print(l2)
#
#
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# func1=lambda x:sorted(x)
# func2=lambda x:sorted(x,reverse=True)
#
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# l1=[]
# l2=[]
# for i in foo:
#     if i>=0:
#         l1.append(i)
#     else:
#         l2.append(i)
# l1=func1(l1)
# l2=func2(l2)
#
# l3=l1+l2
# print(l3)
#

# dic={'name':'wjx','age':20}
# l=list([1,2,3])
# s={1,2,3,4}
# str=str('abcdefg')
# t=(1,2,3,4)
#
#
# dic['sex']='male'
# dic.pop('name')
#
# print(dic)
#
# print(l[1:3:2])
# l.append(4)
# l.pop(0)
# l.remove(2)
# print(l)
#
# print(str[1:6:2])
# print(str+'www')
# print(str.strip('a'))
#
# print(t.index(2))
#
#
# s.remove(1)
# s.add(5)
# print(s)


# import time,datetime
#
# print((datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))


# l=['1','2','3']
# l2=[1,2,3]
# dic={}
# dic2=dict(zip(l,l2))
# dic1=dict([(1,2,),(2,3,)])
# print(dic1)
#
# def deco(f):
#     def warrper(*args,**kwargs):
#         print('g')
#         f(*args,**kwargs)
#     return warrper
#
#
#
#
#
#
# @deco
# def f(x):
#     print(x.lower())
#
# f('WW')

#
# s='ABC'
# l=[]
# for i in s:
#     for j in s:
#         s=j+i
#         l.append(s)
# print(l)

#
# s="<a href=www.baidu.com>正则表达式题库</a><a href=www.cdtest.cn></a>"
# print(re.findall(r'href=(.*?)>',s))
#
# s='HELLO PYTHON'
# s2=s.lower()
# s3=s2.split()
# for i in s3:
#     print(i)
#     with open(r'c:\hello.txt','a') as f:
#         f.write(i)
#         f.write('\n')

# l=[5,4,4,3]
# l2=max(l)
#
# l.remove(l2)
# print(max(l))


# l='1.2.3.4.5'
# l0=list(l)
# l0.remove('.')
# print(l0)


# s="现在的时间是：2018-3-10 1:52"
# print(re.search(r'\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}',s).group())

a=[1,2,3]
b=[4,5,6]
a.sort(reverse=True)
print(a)

a=[1,2,3]
a.reverse()
print(a)


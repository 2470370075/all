import time
import datetime
import random



#
# def f(n):                                               #递归
#     print('抱着',end='')
#     if n > 0:
#         f(n-1)
#         print('的我', end='')
#     else:
#         print('我的小鲤鱼', end='')
# f(3)


c=0                                                       #什么什么塔
def f2(n):
    global c
    if n>0:
        f2(n-1)
        print(n)
        print(c)
        c += 1
        f2(n-1)
x=time.time()
f2(32)
y=time.time()
print(c)
print(y-x)

# x=time.time()                                             #二分法
# def f(l,val):
#     low=0
#     high=len(l)-1
#     while low<high:
#         mid=(high+low)//2
#         if l[mid]==val:
#             return mid
#         elif l[mid]>val:
#             high=l[mid]
#         elif l[mid]<val:
#             low=l[mid]
#     return None
# y=time.time()
# l=list(range(0,100000000))
# print(f(l,5000))
# print(y-x)



def t(func):
    def inner(*args,**kwargs):
        x=time.time()
        ret=func(*args,**kwargs)
        y=time.time()
        print(y-x)
        return ret
    return inner

# @t                                                               #冒泡排序
# def f(l):
#     for i in range(len(l)-1):
#         exchange=False
#         for j in range(len(l)-1-i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#                 exchange=True
#         if exchange==False:
#             return l
#     return l
#

# l=list(range(100))
# random.shuffle(l)
#
# f(l)
# print(l)

# def f(l):                                                    #选择排序
#     for i in range(len(l)):
#         min=i
#         for j in range(i,len(l)):
#             if l[j]<l[min]:
#                 min=j
#         l[min],l[i]=l[i],l[min]
#     return l
# l=list(range(100))
# random.shuffle(l)
# print(l)
# f(l)
# print(l)

# def f(l):                                                  #插入排序
#     for i in range(len(l)):
#         tmp=l[i]
#         j=i-1
#         while j>=0 and l[j]>tmp:
#             l[j+1]=l[j]
#             j-=1
#         l[j+1]=tmp
#     return l
# l=list(range(100))
# random.shuffle(l)
# print(l)
# f(l)
# print(l)


# def quick_sort(l,left,right):
#     if left<right:
#         mid=partition(l,left,right)
#         quick_sort(l,left,mid-1)
#         quick_sort(l,mid+1,right)
#
#
# def partition(l,left,right):
#     tmp = l[left]
#     while left<right:
#         while left<right and l[right]>=tmp:
#             right-=1
#         l[left]=l[right]
#         while left<right and l[left]<=tmp:
#             left+=1
#         l[right]=l[left]
#     l[left]=tmp
#     return left
#
# l=list(range(100))
# random.shuffle(l)
# print(l)
# quick_sort(l,0,len(l)-1)
# print(l)
# def quick_sort(l,left,right):
#     if left<right:
#         mid=partition(l,left,right)
#         quick_sort(l,left,mid-1)
#         quick_sort(l,mid+1,right)
# @t
# def sort(li):
#     left=0
#     right=len(li)-1
#     quick_sort(l,left,right)
#
#
# def partition(l,left,right):
#     i=random.randint(left,right)                          #防止最坏情况，最左面随便往里交换
#     l[left],l[i]=l[i],l[left]
#     tmp=l[left]
#     while left<right:
#         while left<right and l[right]>tmp:
#             right-=1
#         l[left]=l[right]
#         while left<right and l[left]<tmp:
#             left+=1
#         l[right]=l[left]
#     l[left]=tmp
#     return left
# l=list(range(100))
# random.shuffle(l)
# print(l)
# sort(l)
# print(l)




def shift(l,low,high):
    i = low
    j = 2 * i + 1
    while j<= high:
        if j<high and l[j+1]>l[j]:
            j+=1
        if l[i]<l[j]:
            l[i], l[j] = l[j], l[i]
            i = j
            j = 2 * i + 1
        else:
            break

def dsort(l,):
    n=len(l)
    for i in range(n//2-1,-1,-1):
        shift(l,i,n-1)
    for i in range(n-1,-1,-1):
        l[0],l[i],=l[i],l[0]
        shift(l,0,i-1)


l=list(range(100))
random.shuffle(l)
print(l)
dsort(l)
print(l)






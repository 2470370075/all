# class List(list):                                     #改装
#
#     def append(self, obj):
#         if isinstance(obj,int):
#             super().append(obj)
#         else:
#             print('no')
#
#     @property
#     def mid(self):
#         return self[len(self)//2]
#
#     def clear(self):
#         s=input('password:')
#         if s=='123':
#             super().clear()
#         else:
#             print('no')
#
#     @mid.deleter
#     def mid(self):
#         print('有人想删除')
#
#
#
# l=List([1,2,3])
#
# del l.mid
#
# print(l.mid)
# l.append(1)
# print(l)
#
#
# print(hasattr(l,'clear'))
# if hasattr(l,'clear'):
#     name=input('name:')
#     setattr(l,'name',name)
#
#
# l.clear()
# print(l)
# print(getattr(l,'name','不存在'))



# class Foo():
#
#     def __init__(self,name='1'):
#         self.name=name
#
#     def __getitem__(self, item):                             #对象加中括号加字符串运行
#         print('有人想查询！')
#         getattr(self,item)      #反射
#
#     def __setitem__(self, key, value):
#         print('有人想设置！')
#         setattr(self,key,value)
#
#     def __delitem__(self, key):
#         print('有人想删除！')
#         delattr(self,key)
#
#
#     def __del__(self):                                        #删除时运行
#         print('对象被删除')
#
# f=Foo()
# print(f.__dict__)
# print(f.name)
# f['name']='wjx'
# print(f.name)
# f['name']='jxw'
# print(f.name)
# del f['name']
# print(f.__dict__)



#
# class Foo():
#     name='wjx'
#
#     def __getattr__(self, item):                                      #兜底
#         print('没找到',item)
#
#     def __setattr__(self, key, value):
#         print('set了',key,value)
#
#
#     def __call__(self, *args, **kwargs):                               #对象加括号
#         print('hello')
#
# f=Foo()
#
# f.name='111'
# f()
# Foo()()
#
# class Foo():
#     def __new__(cls):
#             if not hasattr(cls, 'ins'):
#                 cls.ins = super().__new__(cls)
#             return cls.ins
#
# f1=Foo()
# f2=Foo()
# print(f1 is f2)
# f1.name='wjx'
# print(f2.name)
#


class Foo():                       #私有变量，类自己里面用，子类也不行
    def __init__(self,name,age):
        self.name=name
        self.__age=age

foo=Foo('wjx',22)
print(foo._Foo__age)            #私有变量只能这么取
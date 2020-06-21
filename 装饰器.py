
from functools import wraps

def enh(arg):
    def deco(func):
        @wraps(func)
        def warrper(*args,**kwargs):
            print('开始了')
            print('外面传入一个参数',arg)
            ret = func(*args,**kwargs)
            print('结束了')
            return ret
        return warrper
    return deco



@enh(8)  #f1=enh(f1)
def f1(x):
    print('我是原函数,我叫{}'.format(x))


f1(3)
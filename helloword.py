class List(list):
    def append(self,x):
        if isinstance(x,int):
            super().append(x)
        else:
            print('不能添加非数字')

    @property
    def mid(self):
        return self[len(self)//2-1]

    def clear(self):
        p=input('要清空的话请输入密码：')
        if p=='123':
            super().clear()
        else:
            print('不让你清空')


l=List([1,2,3])
print(l)
l.append(1)
print(l)

print(l.mid)
# l.clear()
# print(l)


print(hasattr(l,'age'))
setattr(l,'age',18)
print(getattr(l,'age','不存在'))
print(hasattr(l,'age'))

from django.test import TestCase

# Create your tests here.

class Foo():
    def __init__(self,l):
        self.l=l

    def push(self,num):
        self.l.insert(0,num)

    def pop(self,):
        self.l.pop()

queue=Foo([1,2,3])

queue.push('a')
print(queue.l)
queue.pop()
print(queue.l)


class Foo():
    def __init__(self,l):
        self.l=l

    def push(self,num):
        self.l.append(num)

    def pop(self,):
        self.l.pop()

z=Foo([1,2,3])

z.push('a')
print(z.l)
z.pop()
print(z.l)
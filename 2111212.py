import random
import conten

con=conten.content
ans=conten.answer
pri=conten.prize




class question:

    def __init__(self):
        self.id=self.creat()
        self.content=con[self.id]
        self.answer=ans[self.id]
        con.pop(self.id)


    def creat(self):
        id=random.randint(1,20)
        if id in con:
            return id
        if id not in con:
            return self.creat()



class student:

    def __init__(self,name):
        self.name=name

    def answer(self,):
        for i in range(1,6):
            print('%s:'%i,end='')
            ex=question()
            print(ex.content)
            stu_a=input('please answer(A B C D):')

            if stu_a==ans[ex.id]:
                global right
                right+=1

            with open ('1.html','a') as w:
                w.write('%s:%s\n'%(ex.id,stu_a))

right=0
x=input('your name:')
with open ('1.html','a',encoding='utf-8') as w:
    w.write('【%s】\n'%(x))
s1=student(x)
s1.answer()
print('%s分'%(20*right))
if right>=3:
    print('prize')
    p=random.randint(1,3)
    print(pri[p])

else:
    print('you get video')

phonenum=input('your phonenum:')
with open ('1.html','a',encoding='utf-8') as w:
    w.write('【%s】\n'%(phonenum))


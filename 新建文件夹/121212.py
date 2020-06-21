import datetime

from datetime import datetime, timedelta

from time import sleep




def doFunc():
    with open('用户的钱.txt','r') as r:
        data=(r.read())

    with open('list.txt','a')as w:
        d=str(datetime.now())
        w.write(d)
        w.write('\n')
        w.write(data)
        w.write('===================')
        print(d)
        print (data)

def doFirst():
    curTime = datetime.now()

    print(curTime)
    desTime = curTime.replace(day=19,hour=11, minute=38, second=0, microsecond=0)
    print(desTime)
    delta = desTime-curTime
    print(delta)
    sleeptime = delta.total_seconds()
    print("Now day must sleep %s seconds" %(delta))
    sleep(sleeptime)
    doFunc()

doFirst()
while 1:
    sleep(1036800)
    money={}

    with open('额度.txt','r') as r:
        data=r.read()
        data=int(data)
        x=data
    with open('用户的钱.txt','r') as r :
        for i in r:
            (key,value)=i.strip().split(':')
            money[key]=value
    for i in money:
        if money[i] < x:
            cha=x-money[i]
            kou=0.01*cha
            money[i]=money-kou
        with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                for i in money:
                    tm.write('%s:%s\n'%(i,money[i]))
    sleep(864000)
    doFirst()

shoplist={'apple':5,
          'mac':20}
money={}
with open('用户的钱.txt','r') as r :
    for i in r:
        (key,value)=i.strip().split(':')
        money[key]=value

k={}
with open('账户信息.txt','r') as r :
    for i in r:
        (key,value)=i.strip().split(':')
        k[key]=value

with open('额度.txt','r') as r:
    data=r.read()
    data=int(data)
    x=data

yon='no'

def deco(func):                                                                                                         #用户登录
    def wrapper(*args,**kargs):
        global yon
        if yon =='no':
            global name
            global password
            print('=====>请登录《=====')
            name=input('请输入用户名：')
            password=input('请输入密码：')
            if name in k and password==k[name]:
                with open('账单.txt','a',encoding='utf-8') as w :
                    w.write('=======》%s已登录《=======\n'%(name))
                yon='yes'
                func()
            else:
                print('密码错误')
        else:
            func()
    return wrapper

@deco
def turn():
    inname=input('给谁转账：\n')
    m=input('转多少：\n')
    if m.isdigit():
        m=int(m)
        if inname in money:
            money[inname]=int(money[inname])+m
            money[name]=int(money[name])-m
            print('你现在有{}钱，他现在有{}钱'.format(money[name],money[inname]))
            with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                        for i in money:
                            tm.write('%s:%s\n'%(i,money[i]))
            with open ('账单.txt','a',encoding='utf-8') as w :
                    w.write('你给{}转了{}钱\n'.format(inname,m))
            print('=====================================')
        else:
            print('查无此人')
    else:
        print('请输入数字')
@deco
def buy():                                                                                                              #购物函数
    global money
    print('购物列表：%s'%shoplist)
    item=input('你要买什么？\n')
    if item=='apple':
        money[name]=int(money[name])-5
        print('您买了个苹果5元，余额%s'%(money[name]))
    elif item=='mac':
        money[name]=int(money[name])-20
        print('您买了个mac 5元，余额%s'%(money[name]))
    else:
        print('请重新输入')
        item=input('你要买什么？\n')
        buy(item)
    print('=====================================')
    with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                for i in money:
                    tm.write('%s:%s\n'%(i,money[i]))
    with open ('账单.txt','a',encoding='utf-8') as w :
            w.write('您买了个%s\n'%item)
@deco
def manange():                                                                                                          #帐户管理函数
    global  yon
    if name == 'wjx' and password=='123':
        do=input('你要干嘛?(添加账户，冻结账户，用户额度调整）\n')
        if do == '冻结账户':
            newname=input('请输入想要冻结的用户名：')
            newpassword=input('请输入他的密码：')
            if newname in k:
                k.pop(newname)
                print('新的用户信息为：',k)
                with open ('账户信息.txt','w',encoding='utf-8') as tzh:
                    for i2 in k:
                        tzh.write('%s:%s\n'%(i2,k[i2]))
                print('==============================')
                yon='no'
                with open ('账单.txt','a',encoding='utf-8') as w :
                    w.write('冻结了用户：%s\n'%newname)
            else:
                print('查无此人')
        if do == '用户额度调整':
            newx=input('请新的输入信用卡额度：')
            if newx.isdigit():
                newx=int(newx)
                with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                    for i in money:
                        tm.write('%s:%s\n'%(i,int(newx-x+int(money[i]))))
                print('新的信用卡额度为%s\n'%newx)
                print('==============================')
                with open ('额度.txt','w',encoding='utf-8') as w :
                    w.write(str(newx))
                with open ('账单.txt','a',encoding='utf-8') as w :
                    w.write('用户额度调整为：%s\n'%newx)
            else:
                print('请输入数字')

        if do == '添加':
            newname=input('请输入新用户名：')
            newpassword=input('请输入新密码：')
            k.update({newname:newpassword})
            print('新的用户信息为：',k)
            money.update({newname:15000})

            with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                for i in money:
                    tm.write('%s:15000\n'%(i))
            with open ('额度.txt','w') as w:
                w.write(str(x))

            with open ('账户信息.txt','w',encoding='utf-8') as tzh:
                for i2 in k:
                    tzh.write('%s:%s\n'%(i2,k[i2]))
            print('==============================')
            with open ('账单.txt','a',encoding='utf-8') as w :
                w.write('添加了新用户：%s\n'%newname)
            yon='no'

    else:
        print('你不是管理员')
        print('==============================')
        yon='no'

@deco
def exit():                                                                                                             #退出函数
    global yon
    yon='no'
    print('账号已退出')
    print('==============================')


@deco
def ask():
    global money                                                                                                        #取钱函数
    global asknum
    asknum=(input('你想取多少？\n').strip())
    if asknum.isdigit():
        asknum=int(asknum)
        if asknum < int(money[name]):
            money[name]=(int(money[name])-asknum)
            print('信用卡余额：%s'%money[name])
            print('==============================')
            with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                    for i in money:
                        tm.write('%s:%s\n'%(i,money[i]))
            with open ('账单.txt','a',encoding='utf-8') as w :
                w.write('您取走%s元\n'%asknum)
        else:
            print('余额不足')
    else:
        print('请输入数字')

@deco
def repay():
    global money
    repaynum=input('你想还多少？\n')
    if repaynum.isdigit():
        repaynum=int(repaynum)
        money[name]=int(money[name])+repaynum
        print('余额：%s'%money[name])
        with open ('用户的钱.txt','w',encoding='utf-8') as tm :
                    for i in money:
                        tm.write('%s:%s\n'%(i,money[i]))
        print('============================')
        with open ('账单.txt','a',encoding='utf-8') as w :
                w.write('您还了%s元\n'%repaynum)
    else:
        print('请输入数字')



while 1:

    need=input('你需要什么？（取钱，还钱，购物，转账，管理,退出账户）\n')
    if need=='取钱':
        ask()
    elif need=='还钱':
        repay()
    elif need=='购物':
        buy()
    elif need=='管理':
        manange()
    if need=='退出账户':
        exit()
    if need=='转账':
        turn()





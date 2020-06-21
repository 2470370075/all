import random

class hero:
    def __init__(self,life,a,mana):
        self.life=life
        self.a=a
        self.mana=mana
    def at(self,e):
        x=random.randint(-1,1)
        e.life=e.life-self.a+x
        print('【敌人生命减少%s点】'%(self.a+x))

class 斧王(hero):
    camp='yeyan'
    def skill(self,e):
        if self.mana>=10:
            self.mana-=10
            e.life=int(0.8*e.life)
            print('【敌人生命减少%20，自己魔法少10点】')
        else:
            print('#### 没有魔法 ####')
    def skill2(self,e):
        if self.mana>=20:
            self.mana-=20
            if e.life<=15:
                e.life=-1
                print('【敌人生命低于15，直接死亡】')
            else:
                print('【敌人生命高于15，没有效果】')
        else:
            print('#### 没有魔法 ####')

class xiaohei(hero):
    camp='yeyan'
    def skill(self,e):
        if self.mana>=35:
            self.mana-=35
            e.life=int(0.7*e.life)
            print('【敌人生命减少%30，自己魔法少35点】')
        else:
            print('#### 没有魔法 ####')

class fengxing(hero):
    camp='tianhui'
    def skill(self,e):
        if self.mana>=20:
            self.mana-=20
            print('【敌人生命减少%40，自己魔法少20点】')
            e.life=int(0.60*e.life)
        else:
            print('#### no mana ####')
    def skill2(self,e):
        if self.mana>=40:
            self.mana-=40
            print('【敌人生命减少16点，自己魔法少40点】')
            e.life-=16
        else:
            print('#### 没有魔法 ####')


斧王=斧王(65,5,30)
小黑=xiaohei(35,11,80)
风行=fengxing(30,12,45)


def p():
    print('\n%s:\n     生命值:%s 魔法值：%s'%(player1,p1.life,p1.mana))
    print('%s:\n     生命值:%s 魔法值：%s'%(player2,p2.life,p2.mana))


print('小黑:\n     生命值:%s 魔法值：%s 攻击力：10-12'%(小黑.life,小黑.mana))
print('风行:\n     生命值:%s 魔法值：%s 攻击力：11-13'%(风行.life,风行.mana))
print('斧王:\n     生命值:%s 魔法值：%s 攻击力：4-6'%(斧王.life,斧王.mana))


player1=input('选择英雄：')
if player1=='斧王':
    p1=斧王
if player1=='风行':
    p1=风行
if player1=='小黑':
    p1=小黑


player2=input('选择英雄：')
if player2=='斧王':
    p2=斧王
if player2=='风行':
    p2=风行
if player2=='小黑':
    p2=小黑
p2.life+=8

print('\n\n《《《《《游戏开始》》》》》》')
print('%s:\n     生命值:%s 魔法值：%s'%(player1,p1.life,p1.mana))
print('%s:\n     生命值:%s 魔法值：%s'%(player2,p2.life,p2.mana))

while 1:

    print('《======= %s 回合 =======》'%(player1))
    if player1=='斧王'or player1=='风行':
        x=input('    如何进攻(技能 技能2 平a）\n')
        if x=='技能':
            p1.skill(p2)
        if x=='技能2':
            p1.skill2(p2)
        if x=='平a':
            p1.at(p2)
        p()
    else:
        x=input('    如何进攻(技能 平a）\n')
        if x=='技能':
            p1.skill(p2)

        if x=='平a':
            p1.at(p2)
        p()
    if p2.life<=0:
            print('\n=====》%s死了《======'%(player2))
            break

    print('《======= %s 回合 =======》'%(player2))
    if player2=='斧王'or player2=='风行':
        x=input('    如何进攻(技能 技能2 平a）\n')
        if x=='技能':
            p2.skill(p1)
        if x=='技能2':
            p2.skill2(p1)
        if x=='平a':
            p2.at(p1)
        p()
    else:
        x=input('    如何进攻(技能 平a）\n')
        if x=='技能':
            p2.skill(p1)
        if x=='平a':
            p2.at(p1)
        p()
    风行.mana+=10
    if p1.life<=0:
            print('\n》=====%s死了《======'%(player1))
            break

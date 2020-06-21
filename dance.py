import random
import time
scroce=0

while 1:
    num = random.randint(1, 4)
    if num==1:
        need='w'
    if num==2:
        need = 's'
    if num==3:
        need = 'a'
    if num==4:
        need = 'd'
    print(need)
    press=input('')
    if time.clock()>7:
        print('得分:',scroce)
        break
    if press==need:
        print('得分+1')
        scroce+=1
    else:
        print('得分不加一')
    if time.clock()>7:
        print('得分:',scroce)
        break

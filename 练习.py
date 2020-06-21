
#
# res='wjx' if 1==2 else 'jxw'
# print(res)
#
#
#


# sheng=('第{}个'.format(i) for i in range(5))
# print(next(sheng))
# print(next(sheng))
# print(next(sheng))
# print(next(sheng))
# print(next(sheng))

#
#
# import time
# l=[1,2,10,30,33,99,101,200,301,311,402,403,500,900,1000]
# def search(n,l):
#     mid=l[len(l)//2]
#     try:
#         if n>mid:
#             l=l[len(l)//2:]
#
#             search(n,l)
#         elif n<mid:
#             l=l[:len(l)//2]
#             search(n,l)
#
#         elif n==mid:
#             print('find')
#             print(l[len(l)//2])
#
#     except:
#         print('找不到')
#
# s=time.time()
# search(1000,l)
# e=time.time()
# print(e-s)


l1=[{'name':'wjx1','hobby':'swimming1'},
    {'name': 'wjx1', 'hobby': 'swimming2'},
    {'name': 'wjx2', 'hobby': 'swimming3'},
    {'name': 'wjx2', 'hobby': 'swimming4'}]

l2=[]
for i in l1:
    for j in l2:
        if i['name'] == j['name']:
            j['hobbylist'].append(i['hobby'])
            break
    else:
        l2.append({'name':i['name'],'hobbylist':[i['hobby']]})

print(l2)

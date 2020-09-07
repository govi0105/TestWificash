# i=1
# li=[34,41,2,4,42,5,7,67,658,78]
# while i<11 :
#     print('*',end=' ')
#     i+=1
# print('')
# """
# for i in range(2,10,2):
#     print(i)
# for i in li:
#     print(i)
# for i in range(len(li)):
#     print(i)
# """
# number1 = [1,2,3,4,]
# week1 =['星期一','星期二','星期三','星期四']
# for a,b in zip(number1,week1):
#     print(a,b)
# list = [1,2,3,4,5]
# se1 = {1,2,3,4,5}
# se2 = {1,2,3}
# tupple = (1,2,3)
# dictionary = {'name':'1','age':'2','weight':'3'}
# s1 = set(list)
# print(s1)
# s1 = set(tupple)
# print(s1)
# s1 = set(dictionary)
# print(s1)
# print(se2.issubset(se1))
# print(se1.issuperset(se2))
# print(se1.isdisjoint(se2))
# se2.update(se1)
# print(se2)
# se2.update([6,7])
# print(se2)
# let = ['a','b','c','d','e','f','g']
# for num,lets in enumerate(let):
#     print(lets,'is',num+1)
# i=1
# for i in range(1,101):
#     if  i//10==7 or i%7==0 or i%10==7 :
#         print(i,end=' ')
    # elif i%7==7 :
    #     print(i,end=' ')
    # elif i/10==7 :
    #     print(i,end=' ')
    # else:
    #     pass
# l1 = ["sun","mon","tue","wed","thu","fri","sat"]
# l2 = ["sun","mon","thu","sat","we"]
# l3 = []
# s1 = set(l1)
# s2 = set(l2)
# s3 = s1.symmetric_difference_update(s2)
# print(s1)
# l3=s3
# print(l3)
# for i in range(len(l1)):
#     if l1[i] not in l2:
#        l3.append(l1[i])
# for i in range(len(l2)):
#     if l2[i] not in l1:
#        l3.append(l2[i])
# print(l3)

# dict = {'张三':['上海','北京','广州'],'李四':['九寨沟']}
# mane = input('请输入名字：')
# if mane in dict.keys():
#     print(mane)
#     print(dict[mane])
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print('')
# list = []
# for i in range(2,100):
#     for j in range(2,i+1):
#         if  i%j==0 and i!=2 :
#             break
#         else:
#             list.append(i)
#             break
# print(list)
# sum = 0
#
# for i in range(1,65):
#     sum += 2**i
# print(sum*0.00001,'kg')
# for x in range(0,34):
#     for y in range(0,21):
#         z=100-x-y
#         if z % 3 == 0 and x*3+y*5+z/3=100 :
#             print(x,y,z)
# li=[]
# l = 0
# n=int(input("请输入你消费的金钱："))
# for x1 in range(0,4):
#     for x2 in range(0,10):
#         for x3 in range(0,21):
#             for x4 in range(0,100):
#                 m = 25*x1+10*x2+5*x3+x4
#                 m2 =(x1+x2+x3+x4)
#                 if m+n==100:
#                     li.append(m2)
#                     print("找回硬币数：",m2,"个", end=' ，')
#                     print("25美分数：",x1,"个", end=' ，')
#                     print("10美分数：",x2,"个", end='， ')
#                     print("5美分数：",x3,"个", end=' ，')
#                     print("1美分数：",x4,"个")
#                     break
# print(li)
# print("最少硬币数：",min(li))
li=[]
mi={}
n=int(input("请输入你消费的金钱："))
for x1 in range(0,4):
    for x2 in range(0,10):
        for x3 in range(0,21):
            for x4 in range(0,100):
                m = 25*x1+10*x2+5*x3+x4
                m2 =(x1+x2+x3+x4)
                if m+n==100:
                    li.append(m2)
                    ni='25美分数:'+str(x1)+',10美分数:'+str(x2)+',5美分数:'+str(x3)+',1美分数:'+str(x4)
                    mi[m2]=ni
                    # print("硬币数：",m2,"个", end=' ，')
                    # print("25美分数：",x1,"个", end=' ，')
                    # print("10美分数：",x2,"个", end='， ')
                    # print("5美分数：",x3,"个", end=' ，')
                    # print("1美分数：",x4,"个")
                    break
print(li)
print(mi)
minnum=min(li)
print("最少硬币数：",minnum)
print("对应的面值为:"+mi[minnum])




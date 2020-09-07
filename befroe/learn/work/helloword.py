"""print('Hello World!')
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
"""
"""
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))
"""
"""
# 生成 0 ~ 9 之间的随机数

# 导入 random(随机数) 模块
import random

print(random.randint(0, 9))
#随机数字小游戏
import random
i = 1
a = random.randint(0,100)
b = int( input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第%d输入的数字小于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    else:
        print('你第%d输入的数字大于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    i+=1
else:
    print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样'%(i,b))
"""
""""
import datetime
import time

def myday():
    day1=time.time()
    return day1

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
print(getYesterday())
print(myday())

import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
import random
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print(random.choice(list1))
print(random.choice(list2))
"""
#coding=utf-8
# 导入re模块
import re
# 使用match方法进行匹配操作
result = re.match("22","22.cn.22")
print(result.group())
# 如果上一步匹配到数据的话，可以使用group方法来提取数据

ret = re.match(".","M")
print(ret.group())

ret = re.match("t.o","too")
print(ret.group())

ret = re.match("t.o","two")
print(ret.group())
#!/usr/bin/python3
import re
import os
#替换
phone = '18898537584 #这是我的电话号码'
print('我的电话号码:',re.sub('#.*','',phone)) #去掉注释
print(re.sub('\D','',phone))
#search
ip_addr = re.search('(\d{3}\.){1,3}\d{1,3}\.\d{1,3}',os.popen('ifconfig').read())
print(ip_addr)
#match
a = re.match('\d+','2ewrer666dad3123df45')
print(a.group())
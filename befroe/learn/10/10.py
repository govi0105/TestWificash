import _thread,time
from  subprocess import Popen,PIPE
# def fun1():
#     print('43243,%s' %time.ctime())
# def main():
#     _thread.start_new_thread(fun1,())
#     _thread.start_new_thread(fun1,())
#     time.sleep(2)
# if __name__=='__main__':
#     main()
# def ping_check():
#     check = Popen(['/bin/bash','-c','ping -c 2 '+'35.154.129.44'],stdin=PIPE,stdout=PIPE)
#     data = check.stdout.read()
#     print(data)
# ping_check()

# ad={}.fromkeys(['name','age'],'ewe')
# print(ad.get('fhsg','haha'))
# a,*b,c='abcd'
# print(a,b,c)
# print(bool('htrh htheth reyr '))
# x = 1
# sum=0
# words = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1, 100,2):
#     print(i)
#     sum+=i
# print(sum)
# print(sum(i ** 2 for i in range(10)))

# f = open(r'F:\\productCode.txt','w')
# f.write("你好,今天温度特别低，空气很好")
# print(f.seek(10))
# f.close()
# f = open(r'F:\\productCode.txt')
# print(f.read(5))
# print(f.read(3))
# print(f.read(3))
# print(f.read(5))
# def process(string):
#     print('Processing:', string)
# with open('F:\\productCode.txt') as f:
#     char = f.read(1)
#     while char:
#         process(char)
#         char = f.read(1)
# with open('F:\\productCode.txt') as f:
#     while True:
#         line = f.readline()
#         if not line: break
#         process(line)
# with open('F:\\productCode.txt') as f:
#     for char in f.read():
#         process(char)
# import fileinput
# for line in fileinput.input('F:\\productCode.txt'):
#     print(line)



#
# import unittest, myMath
# class ProductTestCase(unittest.TestCase):
#     def test_integers(self):
#         for x in range(-10, 10):
#             for y in range(-10, 10):
#                 p = myMath.product(x, y)
#                 self.assertEqual(p, x * y, 'Integer multiplication failed')
#     def test_floats(self):
#         for x in range(-10, 10):
#             for y in range(-10, 10):
#                 x = x / 10
#                 y = y / 10
#                 p = my_math.product(x, y)
#                 self.assertEqual(p, x * y, 'Float multiplication failed')
# if __name__ == '__main__': unittest.main()
#
#

# import math
# t=math.copysign(1.66, -2.244)
# m=math.factorial(5)
# print(m)
# list00={'a':1,'b':2,'c':3,'d':4,'e':5}
# for a,b in list00.items():
#     print (a)
#     print (b)
# print(all(['a','b','c',True]))
# print(any(['','','',False]))
#
#
#
# x = 10
# expr = """
# z = 50
# sum = x + y + z   #一大包代码
# print(sum)
# """
# def func():
#     y = 20
#     exec(expr)   #10+20+30       输出60
#     exec(expr,{'x':1,'y':2}) #30+1+2         输出 33
#     exec(expr,{'x':1,'y':2},{'y':3,'z':4}) #30+1+3，x是定义全局变量1，y是局部变量  输出34
#
# func()
#
#
# def is_oushu(x):
#     return x%2==1
# new_list=list(filter(is_oushu,list(range(1,11))))
# print(new_list)
# #过滤掉不是偶数的数
# print(hash('test'))      #输出 -2950866779904704330   会改变的
# print(hash(1))              #数字  输出 1
# print(hash(str([1,2,3])))      # 集合   输出 -6217131644886971364
# print(hash(str(sorted({'1':1})))) # 字典   输出 -6233802074491902648
#
#
#
# import copy
#
# #这里有子对象
# numbers=['1','2','3',['4','5']]
# #浅copy
# num1=copy.copy(numbers)
# #深copy
# num2=copy.deepcopy(numbers)
#
# #直接对对象内容进行修改
# num1.append('6')
#
# #这里可以看到内容地址发生了偏移，增加了偏移‘6’的地址
# print('numbers:',numbers)
# print('numbers memory address:',id(numbers))
# print('numbers[3] memory address',id(numbers[3]))
# print('num1:',num1)
# print('num1 memory address:',id(num1))
# print('num1[3] memory address',id(num1[3]))
#
#
# num1[3].append('6')
#
# print('numbers:',numbers)
# print('num1:',num1)
# print('num2',num2)
#
# #1.x是数字
# print(int(2.1))     #输出 2
# print(int(2e3))     #输出 2000
# #print(int(1000,2))       #出错，base 被赋值后函数只接收字符串
# #报错 TypeError: int() can't convert non-string with explicit base
#
# #2.x是字符串
# print(int('abc12',16))    #输出  703506
# #print(int('tuifyg',16))   #出错  tuifyg  超过0-9 abcdef 超出16进制
# #报错 ValueError: invalid literal for int() with base 16: 'tuifyg'
#
# #3. base 可取值范围是 2~36，囊括了所有的英文字母(不区分大小写)，
# # 十六进制中F表示15，那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35
# #print(int('FZ',16))     # 出错，FZ不能用十六进制表示
# #报错 ValueError: invalid literal for int() with base 16: 'FZ'
# print(int('FZ',36))     #  575
#
# #4.字符串 0x 可以出现在十六进制中，视作十六进制的符号，
# # 同理 0b 可以出现在二进制中，除此之外视作数字 0 和字母 x
# print(int('0x10', 16))  # 16，0x是十六进制的符号
# #print(int('0x10', 17)) # 出错，'0x10'中的 x 被视作英文字母 x
# print(int('0x10', 36))  # 42804，36进制包含字母 x
#
#
#
#
# #利用key进行倒序排序
# example_list = [5, 0, 6, 1, 2, 7, 3, 4]
# result_list = sorted(example_list, key=lambda x: x*-22)
# print(result_list)                   #输出  [7, 6, 5, 4, 3, 2, 1, 0]
# print(type(result_list))
class test:
    def __int__(self):
        a = 3
    def compare:
        b = a

# coding=utf-8
import threading  # 导入threading包
from time import sleep
import time


def task1():
    print("Task 1 executed.")
    sleep(1)


def task2():
    print("Task 2 executed.")
    sleep(5)


print("多线程：")
starttime = time.time();  # 记录开始时间
threads = []  # 创建一个线程列表，用于存放需要执行的子线程
t1 = threading.Thread(target=task1)  # 创建第一个子线程，子线程的任务是调用task1函数，注意函数名后不能有（）
threads.append(t1)  # 将这个子线程添加到线程列表中
t2 = threading.Thread(target=task2)  # 创建第二个子线程
threads.append(t2)  # 将这个子线程添加到线程列表中

for t in threads:  # 遍历线程列表
    t.setDaemon(True)  # 将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
    t.start()  # 启动子线程
endtime = time.time();  # 记录程序结束时间
totaltime = endtime - starttime;  # 计算程序执行耗时
print("耗时：{0:.5f}秒".format(totaltime));  # 格式输出耗时
print('---------------------------')
import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:

      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
# import random
# import time
# li1=("面","米粉","米饭","香锅","砂锅","水饺")
# li2=("包子","油条","粥","红薯","玉米","煎饺","蛋饼","茶叶蛋","煎饼")
# li3=("牛奶","酸奶")
# print("我今天早上吃啥："+random.choice(li2)+","+random.choice(li3))
# print("我今天中午吃啥："+random.choice(li1))
# print("我今天晚上吃啥："+random.choice(li1))
# """"
# for i in range(11):
#     time.sleep(1)
#     print(10-i)
# print('闪退')
# time.sleep(1)
# """"" 1 # coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Chrome ()
driver.maximize_window ()
driver.implicitly_wait (6)
driver.get ("http://news.baidu.com")
time.sleep (1)
print(driver.find_elements_by_tag_name ("img"))
for image in driver.find_elements_by_tag_name ("img"):
    print (image.text)
    print (image.size)
print (image.tag_name)
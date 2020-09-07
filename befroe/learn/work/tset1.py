"""
list1 = [1,2,3,4]
print(len(list1))
print(3 in list1)
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print (dict)
print(str(dict))
print(len(dict))
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
info = [1,2,3,4,5,6,7,8,9,10]
#del info[4]
info.append(11)
info.append(12)
"""
# """
# i =1
# while i>0 :
# x =int(input("请输入第一边："))
# y =int(input("请输入第二边："))
# z =int(input("请输入第三边："))
# if x + y > z and  y+z>x and z+x>y:
#     if x == y and y == z:
#         print("能构成等边三角形")
#         break
#     elif x**2+y**2==z**2| z**2+y**2==x**2|x**2+z**2==y**2:
#             if x==y|y==z|z==x:
#                 print("能构成等要直角三角形")
#                 break
#             else:
#                 print("能构成直角三角形")
#                 break
#     else:
#         print("能构成直角三角形")
#         break
# else:
#         print("不能构成三角形，请重新输入：")
#         i+=1
# """"
# import random
# li = ["剪刀","石头","布"]
# i = input("请输入剪刀，石头，布：")
#     if i in li：
#         pass
#     else
#         i = input("请输入剪刀，石头，布：")
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://119.3.19.234/renren-cms/login.html')
driver.find_element_by_xpath("//input[@type='text']").clear()
driver.find_element_by_xpath("//input[@type='text']").send_keys('admin')
driver.find_element_by_xpath("//input[@type='password']").clear()

driver.find_element_by_xpath("//input[@type='password']").send_keys('admin')
driver.find_element_by_xpath("//div[3]/input").clear()
driver.find_element_by_xpath("//div[3]/input").send_keys(input("请输入验证码："))
time.sleep(1)
driver.find_element_by_xpath("//button").click()
print(driver.get_cookies())
time.sleep(2)
#driver.find_element_by_xpath("//div[@id='rrapp']/aside/section/ul/li[4]/ul/li[10]/a").click()
driver.find_element_by_link_text("内容管理").click()
time.sleep(0.5)
driver.find_element_by_link_text("运势管理").click()
time.sleep(0.5)
driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='rrapp']/div/section[2]/iframe"))
driver.find_element_by_xpath("//div[@id='rrapp']/div/div/a[2]").click()
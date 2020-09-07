from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
# 驱动位置 和日志保存位置
driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
#全局等待 隐形等待
driver.implicitly_wait(10)
#d等待
time.sleep(2)
#显性等待
'''
明确了等到某个条件满足之后，再去执行下一步操作
程序每隔XX秒看一眼，如果条件成立了，则执行下一步，否则继续等待
直到超过设置的最长时间，然后抛出TimeoutException

WebDriverWaitlei


'''
WebDriverWait(driver,10,1)
time.sleep(2)


driver.get("http://www.baidu.com")
#窗口大小
driver.maximize_window()



#关闭浏览器会话：1、关闭chromedriver.exe进程；2、关闭浏览器；3恢复些数据环境
#Driver.quit()

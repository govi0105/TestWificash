from selenium import webdriver
from selenium.webdriver.common.by import By
# 驱动位置 和日志保存位置
Driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")

Driver.get("http://www.baidu.com")
#窗口大小
Driver.maximize_window()
#s设置窗口大小
#Driver.set_window_size(1440,900)

Driver.get("http://www.hao123.com")

#返回上一页
Driver.back()
#返回下一页
Driver.forward()
#刷新 （实现第二次访问场景）
Driver.refresh()
#获取当前窗口标题
print(Driver.title)
#获取当前窗口url
print(Driver.current_url)
#获取当前窗口句柄
print(Driver.current_window_handle)

#关闭活跃的窗口 （多个窗口）
Driver.close()

#关闭浏览器会话：1、关闭chromedriver.exe进程；2、关闭浏览器；3恢复些数据环境
Driver.quit()




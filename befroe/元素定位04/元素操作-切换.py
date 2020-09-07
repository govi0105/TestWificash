from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
# 驱动位置 和日志保存位置
driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()

#等待
loc = (By.XPATH,'//div[@tpl="tieba_general"]//a')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))

driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a').click()
time.sleep(1)

# 获取当前所有窗口handles
wins = driver.window_handles
#切换到最后一个窗口--即窗口 ---切换到了一个全新的html页面
driver.switch_to.window(wins[-1])

#切换alert2:先关闭
# #1、弹出来。alert, prompt
# #2. driver. switch_to. alert
# #切换
# #3、关闭弹出框 Alert
driver. get(' D: \\Pychram-Workspace\\python12-web\\myHtml. html')
#点击
driver. find_element_by_id("btn").click()
time.sleep(0.5)
#切换
alert = driver. switch_to.alert
#alert是一个类.1、获取文本提示内容.text; 2, accept()、 dismiss () 3, send keys()
print(alert.text)
alert.accept()


#关闭浏览器会话：1、关闭chromedriver.exe进程；2、关闭浏览器；3恢复些数据环境
driver.quit()

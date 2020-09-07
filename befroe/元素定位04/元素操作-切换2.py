from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
# 驱动位置 和日志保存位置
driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")

driver.get("http://www.baidu.com")

# Fiframe切换
#1、确认你要操作的元素,是否在iframe当中。如果元素在iframa当中,则切换
# #2、先找到这个iframe.等待iframe可见
# WebDriverWait(driver,20).until (EC. visibility_of_element_located((By. XPATH,' //iframe [@r )
# #3、切换framedriver.switch_to.frame("login_frame_qq")#name
# driver.switch_to.frame(driver.find_element_by_xpath('//iframViframe [@name="login_frame_qq"]
# time.sleep (0.5)
# driver. find element_by_id("switcher_plogin").click()1
#4、切换成完成之后, 目前就是以iframe当中的html为主htm2
# #方式二
# webDriverWait (driver, 20).unti1 EC.frame to be_available_andswitch to_it("login_frame_qq")
# time. sleep (0.5)
# driver.find_element-by_id("switcher-plogin"). click()


#设置链接
ele = driver.find_element_by_xpath('//*[@id-"ul"]//a[@name="tj-settingicon"]')
#鼠标悬浮在设置链接上,显示下拉列表。
# #perform()一定要调用。
ActionChains(driver).move_to_element(ele).click(ele).perform()
ele.click()
#//a[text()-"高级搜索"]
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')),driver.find_element_by_xpath('//a[text()="高级搜索"]')).click()

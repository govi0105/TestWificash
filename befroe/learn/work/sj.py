from appium import webdriver
import selenium
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'Appium'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:52001'
desired_caps['appPackage'] = 'com.panshi.ipaisa'
desired_caps['appActivity'] = 'com.panshi.ipaisa.ui.activity.StartActivity'
desired_caps['appWaitActivity'] = '.ui.activity.login.LoginRegitActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element_by_id("com.panshi.ipaisa:id/et_account").send_keys("1230000040") #账号
driver.find_element_by_id("com.panshi.ipaisa:id/et_password").send_keys("123456")  #密码
driver.find_element_by_id("com.panshi.ipaisa:id/loginButton").click() #登录
time.sleep(10)
driver.find_element_by_id("com.panshi.ipaisa:id/tv_me").click()
driver.find_element_by_id("com.panshi.ipaisa:id/tv_help").click()
driver.find_element_by_id("com.panshi.ipaisa:id/tv_type").click()
# driver.find_element_by_id("com.panshi.ipaisa:id/tv_day_02").click() #借款天数选择
# driver.find_element_by_id("com.panshi.ipaisa:id/btn_loan").click()  # 确认借款
# time.sleep(5)
driver.quit()

# driver.find_element_by_name("0").click()
# driver.find_element_by_name("1").click()
# driver.find_element_by_name("8").click()
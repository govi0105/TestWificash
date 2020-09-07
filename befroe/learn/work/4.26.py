# import requests
# r = requests.get("https://www.cnbeta.com/")
# h=r.headers
# b=r.url
# t=r.text
# e=r.encoding
# print(h)
# print(b)
# print(t)
# print(e)
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class test:
    def test_open(self): #打开页面
        driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # 浏览器驱动
        driver.maximize_window()  # 浏览器最大化
        driver.get('http://managetest.wificash.in/index.html')  #打开页面
        time.sleep(20)  # 等待10秒
        sreach_windows = driver.current_window_handle
        d1=driver.find_element_by_xpath("//input[@name='username'][2]")
        d1.clear()
        print(d1)
        driver.find_element_by_xpath("//input[@name='username'][2]").send_keys("gaowei")
        driver.find_element_by_xpath("//input[@name='password'][2]").clear()
        driver.find_element_by_xpath("//input[@name='password'][2]").send_keys("123456123456")
        driver.find_element_by_xpath("//button").click()  #
        time.sleep(5)
        sreach_windows1 = driver.current_window_handle
        print(sreach_windows,sreach_windows1)
        if sreach_windows1 != sreach_windows:
            driver.switch_to.window(sreach.windows1)
            driver.find_element_by_link_text("OK").click()

        #driver.switch_to.prompt().accept()
        time.sleep(20)

x = test() #class类 实例化
x.test_open() #执行class类 register函数

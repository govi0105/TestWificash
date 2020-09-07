'''=================================================
@Project -> File   ：TestWificash -> test_baidu
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/25 17:08
@Desc   ：
=================================================='''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
# 驱动位置 和日志保存位置
Driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
#窗口大小
Driver.maximize_window()

Driver.get("https://www.12306.cn/index/")
# loc =  "//input[id='train_date']"
# WebDriverWait(Driver, 30).until(EC.visibility_of_element_located((By.ID,"fromStationText")))
Driver.implicitly_wait(10)
# 出发站
# t = Driver.find_element_by_xpath("//a[@class='menu-nav-hd']").text
# print(t)
time.sleep(3)
WebDriverWait(Driver, 10).until(EC.visibility_of_element_located((By.ID,"fromStationText")))
Driver.find_element_by_id("fromStationText").click()
Driver.find_element_by_id("fromStationText").send_keys("成都东")
# 模拟键盘操作：回车键
Driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)

# 终点站
Driver.find_element_by_id("toStationText").click()
Driver.find_element_by_id("toStationText").send_keys("重庆北")
Driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)

# 滚动条操作:当待操作的元素在页面可视区域之外,则需要将待操作的元素,滚动到可视区域当中。
# 步骤:1、先查找到元素;element = driver.find_element_by_xxxx("XXX)"
# 2、再将元素拖动到可见区域;通过执行javascript语句实现,driver.execute_script("arguments[0].scrolllntoView():",element) #scrolllntoViewlfneeded
# 3、再操作元素;element.XXXXX)
# 例子:百度搜索

# ele =Driver.find_element_by_id("train_date")
# Driver.execute_script("arguments[0].scrolllntoView();",ele)
# ele.readOnly = "false"
# ele.send_keys("2018-08-29")

js = 'var e = document.getElementById("train_date"); e.readOnly = false ; e.value ="2020-08-30"'
Driver.execute_script(js)

time.sleep(1)
Driver.find_element_by_id("search_one").click()

time.sleep(10)


Driver.quit()

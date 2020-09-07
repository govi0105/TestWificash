from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium. webdriver. common. action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome()
driver.get ("http://www. baidu. com")
#设置链接
ele = driver. find_element_by_xpath(' //* [@id="ul"]//a[@name="tj-settingicon"')
#鼠标悬浮在设置链接上,显示下拉列表。
#perform()一定要调用。
ActionChains(driver).move_to_element(ele).perform()
#//a[text()="高级搜索"]
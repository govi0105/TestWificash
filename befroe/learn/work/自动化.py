from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.get('http://manage.getmoney.club/index.html')
driver.find_element_by_xpath("//button").click()
time.sleep(1)
# driver.find_element_by_xpath("span[contains(.,'产品管理')]").click()
driver.find_element_by_xpath("//div[@id='app']/div/div/div/div/ul/div[3]/li/div").click()

#Select.select_by_value("印度")
# driver.find_element_by_css_selector()
# se.select_by_index(1)
# driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='rrapp']/div/section[2]/iframe"))
# driver.switch_to.frame(driver.find_element_by_xpath("//div[@id='cke_1_contents']/iframe"))
# driver.find_element_by_xpath("html/body/p").send_keys("试试看")
#
# # driver.find_element_by_xpath("//p").send_keys('http://npntc.stayrocky.com/ntcfuncMore/#/  user_phone=9851212538')
# driver.switch_to.default_content()
# driver.find_element_by_xpath("//div[@id='rrapp']/div[2]/form/div[8]/div[2]/input").send_keys('2019/04/02')
# driver.find_element_by_id('thumbnail').send_keys('https://globalstores.blob.core.windows.net/panshiresources/a5f63151-973d-4643-9ef8-bb89414d4d6e.png')
# se = Select(driver.find_element_by_xpath("//div[@id='rrapp']/div[2]/form/div[12]/div[2]/select"))
# se.select_by_index(1)
# se = Select(driver.find_element_by_xpath("//div[@id='rrapp']/div[2]/form/div[13]/div[2]/select"))
# se.select_by_index(1)
# driver.find_element_by_xpath("//div[@id='rrapp']/div[2]/form/div[14]/div[2]/input").send_keys('10.24-11.22')
# driver.find_element_by_xpath("//input[@value='确定']").click()
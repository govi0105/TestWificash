from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
driver =  webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
#全局等待 隐形等待
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://managetest.wificash.in/index.html")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Risk Control Management']")))
driver.find_element_by_xpath("//span[text()='Risk Control Management']").click()
WebDriverWait(driver,20).until (EC. visibility_of_element_located((By. XPATH,"//iframe[contains(@src,'LoanPreliminaryManage')]")))
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'LoanPreliminaryManage')]"))
time.sleep (0.5)
driver.find_element_by_xpath("//input[@name='loginName' and @placeholder='Mobile Number']").send_keys("1230000020")
time.sleep (0.5)
driver.find_element_by_xpath("//button[@data-code='/manage/risk/reviewBorrowList.htm' and @set-lan='html:查询']").click()
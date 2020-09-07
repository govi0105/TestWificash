'''=================================================
@Project -> File   ：python3 -> login_page
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/17 11:02
@Desc   ：登录页面
=================================================='''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Common.basepage import BasePage
class LoginPage:

    def __init__(self,driver):
        #self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",service_log_path="D:/test.log")
        self.driver =driver



    #登录功能
    def login(self,username,passwd):

        loc = (By.XPATH,"//input[@placeholder='Enter Username']")
        model_name = "登录页面"
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        # BasePage.wait_eleVisible(*loc,model_name=model_name)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter Username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@set-lan='placeholder:输入密码']").send_keys(passwd)
        self.driver.find_element_by_xpath("//span[text()='Login']").click()


     # 获取错误提示---没有密码
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'padding')]")))
        return  self.driver.find_element_by_xpath("//div[contains(@class,'padding')]").text


    #获取错误提示---没有密码
    def test_get_errorMsg_noPasswd(self):

        pass
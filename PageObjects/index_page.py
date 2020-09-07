'''=================================================
@Project -> File   ：python3 -> login_page
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/17 11:02
@Desc   ：登录后页面
=================================================='''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class IndexPage:
    def __init__(self, driver):

        self.driver = driver

    def isExist_quitEle(self):
        try:
            #等15
            time.sleep(2)
            self.driver.refresh()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[text() = 'Welcome']")))
            return True
        except:
            return False


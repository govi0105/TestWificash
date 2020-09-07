'''=================================================
@Project -> File   ：TestWificash -> login_msg_page
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/25 16:48
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
class IndexMsgPage:
    def __init__(self, driver):

        self.driver = driver

    def login_msg(self):
        try:
            #等15
            time.sleep(2)
            self.driver.refresh()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class ,'layui-layer-msg')]")))

            return True
        except:
            return False


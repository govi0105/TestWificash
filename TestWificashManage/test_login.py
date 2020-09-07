'''=================================================
@Project -> File   ：python3 -> login_page
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/17 11:02
@Desc   ：登录主程序
=================================================='''
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from selenium import webdriver
from TestDatas.data import Data
import ddt
import pytest

@ddt.ddt
@pytest.mark.smoke
@pytest.mark.login
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(Data.driving)
        cls.driver.maximize_window()
        cls.driver.get(Data.login_url)
        cls.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
       pass
    def tearDown(self):
        self.driver.refresh()
    #登录成功用例
    # def test_login_success(self):
    #
    #     #步骤：登录页面的登录+
    #     LoginPage(self.driver).login("gaowei","g123456123456")
    #     # 断言：首页用户查询
    #     self.assertTrue(IndexPage(self.driver).isExist_quitEle())

    # 登陆失败用例
    @ddt.data(*Data.data)

    def test_login_errorPasswd (self,data):
        #步骤:登陆页面的登陆功能
        lp = LoginPage(self. driver)
        lp.login(data["username"],data["passwd"])
        #断言:登陆页面的错误提示是否正确
        self.assertEqual(data["msg"],lp.get_errorMsg_from_loginArea())
        print(data["msg"],"测试通过")
    # def test_login_noUser(self):
    #     pass
    #     #步骤:登陆页面的登陆功能
    #     lp = LoginPage(self.driver)
    #     lp.login("","python")
    #     #断言
    #     self. assertEqual ("请输入用户名", lp.get_errorMsg_from_loginArea())
    # def test_login_user_less11 (self):
    #     #步骤:登陆页面的登陆功能
    #     lp = LoginPage (self.driver)
    #     lp.login("python", "g123456123456")
    #     self.assertEqual ("请输入正确的用户名",lp.get_errorMsg_from_loginArea())

        # driver.implicitly_wait(10)
        # a = driver.find_element_by_css_selector('layui-layer-content.layui-layer-padding').get_attribute('textContent')
        # print(a)
'''=================================================
@Project -> File   ：TestWificash -> data
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/27 20:13
@Desc   ：
=================================================='''
class Data:
    #登录数据
    data = [
        {"username": "","passwd": "e122rewr54","msg":"user name cannot have special characters"},
        {"username": "12245454","passwd": "e122rewr54","msg":"user name cannot all be numbers"},
        {"username": "gaowei","passwd": "e1r4","msg":"password must be 6-24 bits long and no spaces are allowed"},
        {"username": "gaowei","passwd": "1234546565465","msg":"Password error, please check and enter"}]
    #驱动位置
    driving ="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
    # 登录地址
    login_url ="http://managetest.wificash.in/pages/login/login.html"

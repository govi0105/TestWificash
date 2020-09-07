from selenium import webdriver
import select
import time
driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
#
def test1():
    driver.get('http://managetest.wificash.in/pages/login/login.html')
    driver.find_element_by_xpath("//input[@name='username'][2]").clear()
    driver.find_element_by_xpath("//input[@name='username'][2]").send_keys('gaowei')
    driver.find_element_by_xpath("//input[@name='password'][2]").clear()
    driver.find_element_by_xpath("//input[@name='password'][2]").send_keys('123456123456')
    driver.find_element_by_xpath("//button").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[3]/dl/dd[4]/a/span').click()
    driver.implicitly_wait(20)
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@lay-item-id='15']/iframe"))
    driver.find_element_by_xpath('//*[@id="queryAuditJS"]/form/div[3]/div').send_keys('1230000007')
    driver.find_element_by_xpath('//*[@id="Query"]').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[3]/div[2]/table/tbody/tr[1]').click()
    Select(driver.find_element_by_xpath('//*[@id="AddAllotJS"]/div/div[1]/div[2]/div/div/div/input')).select_by_visible_text("高伟")
    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()

    # driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/iframe"))
    # driver.implicitly_wait(30)

test1()
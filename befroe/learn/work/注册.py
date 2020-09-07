from selenium import webdriver
import time
import csv
import  pymysql
date = csv.reader(open("F:\denglu.csv",'r'))
def getConn():
    conn = pymysql.connect(host='104.211.72.241', user='qqyd_hujin', password='MUUC#QuuKBUs', db='indialoan_preview_wificash', charset='utf8')
    return conn
def searchAll(newphone):#执行查询所有数据
    conn=getConn()
    cursor=conn.cursor()
    sql1="select SUBSTR(code,1,4) from cl_sms where phone="+newphone+" and sms_type = 'register' order by id desc limit 1"
    cursor.execute(sql1)
    code=cursor.fetchall()
    # showPhoneandCode(data)
    # wrterdata(data)
    cursor.close()
    conn.close()
    print(code)
    return  code
for user_phone in date:
    pass
    for i in range(len(user_phone)):
        phone = user_phone[i]
        print(phone)
        code = searchAll(phone)
        print(code)

        driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver.maximize_window()
        driver.get('http://apitest.wificash.in/html')
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys(phone)
        code = searchAll(phone)
        # print(code)
        driver.find_element_by_id("otp").clear()
        driver.find_element_by_id("otp").send_keys(code)
        driver.find_element_by_id("sendOTP").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(123456)
        driver.find_element_by_id("register").click()
        driver.quit()

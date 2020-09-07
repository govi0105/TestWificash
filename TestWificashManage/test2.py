#python 3.6
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding=utf-8
from selenium import webdriver
from Common.basepage import BasePage
import logging
import time

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)

picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filePath = ("D:/TestWificash/Outputs/Screenshots/{}.png".format(picture_time))
try:

    driver.get_screenshot_as_file(
        "D:/TestWificash/Outputs/Screenshots/{}.png".format( picture_time))
    logging.info("截图成功，文件路径为：{}".format(filePath))
except:
    logging.exception("截图失败！！")
driver.quit()
model_name = "百度"
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filePath = ("D:/TestWificash/Outputs/Screenshots/{0}_{1}.png".format(model_name, picture_time))
try:

    driver.get_screenshot_as_file("D:/TestWificash/Outputs/Screenshots/{0}_{1}.png".format(model_name, picture_time))
    logging.info("截图成功，文件路径为：{}".format(filePath))
except:
    logging.exception("截图失败！！")
logging.basicConfig()
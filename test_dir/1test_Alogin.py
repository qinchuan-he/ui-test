# coding=utf-8
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
import os  # 上传autoit用
import sys
import re # 正则提取
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 公共方法
from common.newcomfunction import new_screen_short

# 第二例子

class Testsign():
    '''测试登录'''
    # user = "19925253635"
    pwd = "Test123456"
    user = "13248131618"
    path = ""
    def test_login_case(self, browser, base_url, images_path):
        """ 测试登录"""
        # page = LoginPage(browser)
        # page.get(base_url)
        # page.switch_login.click()
        # page.user_input = "19958585555"
        driver = browser
        driver.get(base_url)
        driver.find_element_by_xpath("//span[text()='账号登录']").click()
        driver.get_screenshot_as_file( images_path+"test_login_case-验证截图-" + str(time.time()) + ".png")
        driver.find_element_by_id("username_no").send_keys(self.user)
        driver.find_element_by_id("password").send_keys(self.pwd)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        # sleep(1.5)
        # driver.find_element_by_xpath("//a[text()='私有资料']").click()
        WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='笔记摘录']")))
        # assert 2+2 == 5

    def test_create(self, browser, images_path):
        ''' 新建文件夹'''
        driver = browser
        el21 = driver.find_element_by_xpath("//span[text()='新建']/..")
        ActionChains(driver).move_to_element(el21).perform()
        driver.find_element_by_xpath("//li[text()='文件夹']").click()
        sleep(0.5)
        driver.switch_to.active_element.send_keys(str(time.time()))
        sleep(0.5)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        new_screen_short(browser, images_path, pic_name="test_create-执行完成")
        sleep(2)
















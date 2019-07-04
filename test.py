#coding=utf-8

import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
import sys
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# from nose_parameterized import parameterized
from parameterized import parameterized

# print(sys.path)
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 引入公共方法
from common.comfunction import execBrower
from common.comfunction import user

class createFile(unittest.TestCase):
    '''创建文件夹'''
    mode = 1
    driver = execBrower(mode)
    user().login(driver)

    # @parameterized.expand(self.driver)
    # print("类变量")
    def test1_create_File(self):



        print("进入方法")
        # self.driver = self.exe
        waitTime=3
        # 私有根目录新建文件夹
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        folder1=int(time.time())
        print("新建文件夹：%s " %folder1)
        self.driver.switch_to.active_element.send_keys(folder1)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        # 进入文件夹
        self.driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()
    def test2_create2(self):
        # self.driver = self.exe
        waitTime=3
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        ActionChains(self.driver).move_to_element(el1).perform()
        sleep(waitTime)
        self.driver.find_element_by_xpath("//li[text()='新建文档']").click()
        print("hhaha")


# t = createFile()
# t.create_File()
# t.create2()
if __name__ == "__main__":
    # unittest.main()
    testunit=unittest.TestSuite()
    testunit.addTest(createFile("test1_create_File"))
    testunit.addTest(createFile("test2_create2"))
        # 报告
    fp = open('C:\\work\\1测试\\10自动化\\报告\\test1.html','wb')
    runner = HTMLTestRunner(stream=fp, title='test报告', description='执行情况：')
    runner.run(testunit)
    fp.close()




















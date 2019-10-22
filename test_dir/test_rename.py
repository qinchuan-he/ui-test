# coding=utf-8
import io
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# 报告
import pytest
# import unittest
# from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
import os  # 上传autoit用
import sys
import re  # 正则提取

"""解决vscode中不能引用别的模块的问题"""
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 引入公共方法
from common.newcomfunction import new_user
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_path
from common.comfunction import team

# 2019/09/30
# 本次验证团队文件夹的重命名，是否更新时间和名字,成员新建，另外成员文件夹内上传，成员再修改名字


#
# mode = 2
class Test_Rename:
    '''私有中重命名文件夹和文件'''
    def test_private(self, browser, base_url, images_path):
        """验证登录并截图"""
        print("base_url:" + base_url)
        new_user().new_login(browser, base_url)
        driver = browser
        folder = str(time.time())
        # User().createFolder(driver, folder)
        sleep(0.5)
        # driver.find_element_by_xpath("//span[text()='"+folder+"']").click()
        # folder2 = str(time.time())
        # # User().createFolder(driver,folder2)
        # # sleep(0.5)
        # # 新建成功截图
        driver.get_screenshot_as_file(images_path + "test_private-新建文件夹成功截图" + str(time.time()) + ".png")
        # # 上传文件

# if __name__ == '__main__':
#     pytest.main(["-sv", "test_rename.py"])























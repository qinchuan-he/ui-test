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
# 引入公共方法
from common.comfunction import execBrower  # 启动浏览器函数
from common.comfunction import user  # 用户登录类
from common.comfunction import comHtml  # 生成html报告类
from common.comfunction import team  # 团队类
from common.comfunction import com_upload # 公共上传函数
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_share  #  分享类公共方法

resultPath = "C:\\work\\1测试\\10自动化\\报告\\"

# 验证移动功能，文件移动，文件夹移动，移动的重名处理
# 移动文件夹，私有，根目录到子目录，子目录到根目录,子目录到子目录（重名，不重名）
# 移动文件夹，团队，根目录到子目录，子目录到根目录，子目录到子目录（重名，不重名）
# 移动文件，私有，子目录到根目录，根目录到子目录，子目录到子目录，移动重名问题（同类型，不同类型）,艾玛文件移动出来
# 移动文件，团队，子目录到根目录，根目录到子目录，子目录到子目录，移动文件重名问题（同类型，不同类型）

class test_move(unittest.TestCase):
    '''验证文件和文件夹的移动'''
    # 公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\移动\\"  # 生成截图路径


    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    def test_moveFolder_private(self):
        '''私有中移动文件夹'''
        folder1 = str(time.time())
        # 子目录到根目录
        user().createFolder(self.driver, folder1)
        self.driver.find_element_by_xpath("//span[text()='"+folder1+"']").click()
        user().createFolder(self.driver, folder1)
        el11 = self.driver.find_elements_by_xpath("//input[@class='ant-checkbox-input']")
        el13 = self.driver.find_element_by_xpath("//span[text()='"+folder1+"']")
        ActionChains(self.driver).move_to_element(el13).perform()
        el11[1].click()
        button = "move"
        el12 = com_xpath().com_listButton(self.driver, button)
        el12.click()
        # 验证移动弹框取消功能
        type = "取 消"
        type1 = "私有"
        com_alert().com_move(self.driver, self.picturePath, type, folder1)
        el12.click()
        type3 = "确 定"
        com_alert().com_move(self.driver, self.picturePath, type3, type1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="移动之后截图")
        self.driver.find_element_by_xpath("//a[text()='私有']").click()
        sleep(1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目:"+folder1+"为移动文件")

    def test_moveFolder_team(self):
        '''移动团队中文件夹'''

if __name__ == "__main__":
    case = unittest.TestSuite()
    case.addTest(test_move("test_moveFolder_private"))

    fp = open(resultPath+"移动功能验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="移动验证报告", description="验证文件夹、文件移动和移动重名")
    runner.run(case)
    fp.close()



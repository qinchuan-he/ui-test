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

"""解决vscode中不能引用别的模块的问题"""
import os
import re # 正则
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

# 分享功能验证，以PDF文件验证，预览中，边写边搜中，艾玛中（碎片分享），文件夹中（工具栏和更多），文件夹内搜索中，比对报告中分享
resultpath = "C:\\work\\1测试\\10自动化\\报告\\"

'''分享功能验证'''
# 公共参数

picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\"
showPath = "file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/"
# 启动浏览器
mode = 2
driver = execBrower(mode)
user().login(driver)
driver.implicitly_wait(30)

# 进入文件夹

driver.find_element_by_xpath("//span[text()='1563182344']/..").click()
sleep(0.5)

driver.find_element_by_xpath("//input[@placeholder='搜文件，也可以通过“#”搜标签']").send_keys("146页年度报告")
driver.switch_to.active_element.send_keys(Keys.ENTER)
el11 = driver.find_elements_by_xpath("//span[text()='私有']/../../..")
el11[0].click()
WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
driver.find_element_by_xpath("//div[contains(@class,'EmmaPage_shareIcon')]").click()















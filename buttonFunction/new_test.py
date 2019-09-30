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
from common.comfunction import User  # 用户登录类
from common.comfunction import comHtml  # 生成html报告类
from common.comfunction import team  # 团队类
from common.comfunction import com_upload # 公共上传函数
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_share  #  分享类公共方法
from common.comfunction import com_path
from common.comfunction import addAttribute

resultPath = com_path()+"报告\\"
# 验证比对功能，比对分为纯文本和图片两种比对

'''测试比对'''
#  公共参数
picturePath = com_path()+"截图\\"+"19种上传格式截图\\other\\"  # 生成截图路径
if not (os.path.exists(picturePath)):
    os.makedirs(picturePath)
uploadPath = com_path()+"19种格式\\比对文件\\" #  上传路径
wordname1 = "合同1"
pdfname1 = "合同"
pdfname2 = "合同1扫描件（8张合并）"
pdfname3 = "36页"  # 后缀是大写的PDF
pdfname4 = "30页图片"
folder = '哇哈哈' #  文件夹名字

# 启动浏览器
mode = 2
driver = execBrower(mode)
User().login(driver)
driver.implicitly_wait(5)
# driver.find_element_by_xpath("//span[text()='哇哈哈']/..").click()
sleep(0.5)
pdfname = "哇哈哈"
team_name = team().check_team(driver)
com_xpath().com_internalSearch(driver, pdfname)
driver.find_element_by_xpath("//span[contains(text(),'协作共')]/../..").click()
sleep(1)
print_name = "文件夹内收藏"
version = "以新版本覆盖"
try:
    WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))  # 未考虑txt
    driver.find_element_by_xpath("//div[contains(@class,'EmmaPage_fileViewBarList')]/div[3]").click()
    sleep(0.5)
    com_alert().com_equal(driver, picturePath, print_name, version)

except Exception as e:
    print(e)
    print("超时未加载出来或者选中为txt")









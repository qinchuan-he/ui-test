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
from  buttonFunction import store
from buttonFunction.moveFile import test_move

resultPath = "C:\\work\\1测试\\10自动化\\报告\\"
case = unittest.TestSuite()
case.addTest(test_move("test_moveFolder_private"))
case.addTest(test_move("test_moveFolder_team"))
case.addTest(test_move("test_moveFile_team"))
case.addTest(test_move("test_moveFile_private"))
case.addTest(test_move("test_quit"))

fp = open(resultPath + "移动功能验证.html", "wb")
runner = HTMLTestRunner(stream=fp, title="移动验证报告", description="验证文件夹、文件移动和移动重名")
runner.run(case)
fp.close()
















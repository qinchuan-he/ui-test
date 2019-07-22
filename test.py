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
from common.comfunction import com_share # 分享按钮点击之后的判断

from buttonFunction.store import test_store

test_store().test_listStore()




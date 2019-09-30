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
import pytest
import unittest
from HTMLTestRunner import HTMLTestRunner
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
# 本次验证团队文件夹的重命名，是否更新时间和名字

upload_url = com_path()+"19种格式\\office\\2017年12月11日-2017年12月15日发行监管部.doc"
upload_url2 = com_path()+"19种格式\\其他\\146页年度报告.PDF"
name = "2017年12月11日-2017年12月15日发行监管部"
name2 = "146页年度报告"

mode = 1
class Test_team_file:
    '''验证团队中文件夹和文件的重命名显示'''

    def test_folder(self, browser, base_url, images_path):
        driver = browser
        new_user().new_login(browser, base_url)
        team_name = team().check_team(driver)

























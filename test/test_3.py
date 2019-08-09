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
import pytest
import math
from test.conftest import test_url
# print(sys.path)
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')  # 有这一句会导致，pytest运行报IO错误

# @pytest.mark.parametrize(
#     "a, b, c",
#     [(1,2,1),
#      (2,2,4),
#      (0,9,1)]
#     # ids=["case1", "case2", "case3"]
# )
# def test_pow(a,b,c,test_url):
#     assert math.pow(a, b) == c
#     # print(test_url)

@pytest.mark.flaky(reruns=5, reruns_delay=1) # 设置失败执行5次，0延迟
def test_baidu():
    sleep(3)
    assert 2 + 2 ==4
def test_bi():
    sleep(2)
    print("hahha")
def test_acf():
    sleep(2)
    print("acfun")
if __name__ == "__main__":
    # pytest.main(['-s'])
    # pytest.main(['-sv',  'test_3.py', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
    # pytest.main(['-sv', 'test_3.py', '--tests-per-worker', 'auto', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
    pytest.main(['-sv', 'test_3.py', '--junit-xml=../test_report/log.xml'])



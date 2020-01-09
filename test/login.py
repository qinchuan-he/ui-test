# coding=utf-8
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
import unittest
# 发送邮件
import smtplib
from email.mime.text import  MIMEText  # 正文
from email.header import Header  # 头部
from email.mime.multipart import MIMEMultipart # 上传附件用
from common.private import UserProperty

# 服务器上传
import paramiko



class MyTest(unittest.TestCase):
    '''验证测试用'''

    def setUp(self):
        path = UserProperty().BROWER_PATH
        url = "https://testcyprex.fir.ai/sign-in"
        self.driver = webdriver.Chrome(path)
        self.driver.set_window_size(1400, 900)
        self.driver.implicitly_wait(10)
        self.driver.get(url)


    def tearDown(self):
        '''退出浏览器'''
        self.driver.quit()
































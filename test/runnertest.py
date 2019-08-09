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
from HTMLTestRunner import HTMLTestRunner
# 服务器上传
import paramiko

resultpath = "C:\\work\\1测试\\10自动化\\报告\\"

if __name__ == "__main__":
    case = unittest.defaultTestLoader.discover(start_dir='test', pattern='testlogin.py')
    fp = open(resultpath+"这次测试setup方法.html", 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试1', description='简单描述')
    runner.run(case)
    fp.close()























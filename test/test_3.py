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
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from common.comfunction import com_path,send_mail
from common.private import EmailProperty
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

# sender = "qinchuan.he@fir.ai"
# recivie = ["m13248131618@163.com","849446261@qq.com"]
# msg = MIMEText("我发送的邮件","plain","utf-8")
# print(sender)
# msg['From'] = sender
# print(','.join(recivie))
# msg['To'] = ','.join(recivie)
# msg['Subject'] ="验证的邮件"
# # Header("","utf-8")
# print(" msg--------:%s" % msg)
# smtp  = smtplib.SMTP("smtp.exmail.qq.com")
# # smtp.connect("smtp.exmail.qq.com")
# smtp.login("qinchuan.he@fir.ai","Test12345678")
# smtp.sendmail("qinchuan.he@fir.ai",["m13248131618@163.com","849446261@qq.com"],msg.as_string())
# smtp.quit()







s=[com_path() + "截图\\" + "合并失败截图.png",com_path() + "截图\\" + "拆分截图.png"]
p=["combine.png","split.png"]

send_mail("合并检查邮件", EmailProperty().EMAIL_COMBINE, com_path() + "截图\\" + "合并失败截图.png",
                              "combine.png")

s1 = com_path() + "截图\\" + "合并失败截图.png"

print(type(s1).__name__)










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

# @pytest.mark.flaky(reruns=5, reruns_delay=1) # 设置失败执行5次，0延迟
# def test_baidu():
#     sleep(3)
#     assert 2 + 2 ==4

# def test_bi():
#     sleep(2)
#     print("hahha")
# def test_acf():
#     sleep(2)
#     print("acfun")
# if __name__ == "__main__":
#     # pytest.main(['-s'])
#     # pytest.main(['-sv',  'test_3.py', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
#     # pytest.main(['-sv', 'test_3.py', '--tests-per-worker', 'auto', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
#     # pytest.main(['-sv', 'test_3.py', '--junit-xml=../test_report/log1.xml'])
#     pytest.main(['-sv', 'test_3.py', '--html=../test_report/log.html'])



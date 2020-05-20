# coding=utf-8
import io
import sys
from selenium import webdriver
# from selenium.webdriver.support.ui import Testrubbish
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
# 发送邮件
import smtplib
from email.mime.text import  MIMEText  # 正文
from email.header import Header  # 头部
from email.mime.multipart import MIMEMultipart # 上传附件用
from common.private import UserProperty
from common.comfunction import *

# from buttonFunction.store import test_store
import unittest

s = 23
t = 3
assert str(t) in str(s)










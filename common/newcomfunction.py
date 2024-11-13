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
# 发送邮件
import smtplib
from email.mime.text import  MIMEText  # 正文
from email.header import Header  # 头部
from email.mime.multipart import MIMEMultipart # 上传附件用

# 服务器上传
import paramiko

# 引入公共参数
from common.comfunction import user
from common.comfunction import url
from common.comfunction import pwd
from common.comfunction import User

# 针对pytest框架的封装---20190903,还是用一部分原来的封装


# pytest的公共截图方法，传入driver，images_path图片存放路径，pic_name图片名字(函数名-目标名字)
def new_screen_short(driver, images_path, pic_name):
    driver.get_screenshot_as_file(images_path + pic_name + "-" + str(time.time()) + ".png")


# 封装user相关方法
class new_user():

    # 登录方法,针对有内容管理权限的账号
    def new_login(self, driver, base_url=None, bae_user=None, base_pwd=None):
        if base_url:
            driver.get(base_url)
        else:
            driver.get(url)
        driver.find_element_by_xpath("//span[text()='账号登录']").click()
        if bae_user:
            driver.find_element_by_id("username_no").send_keys(bae_user)
        else:
            driver.find_element_by_id("username_no").send_keys(user)
        if base_pwd:
            driver.find_element_by_id("password").send_keys(base_pwd)
        else:
            driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        User().root_private(driver)
        try:
            WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='笔记摘录']")))
        except Exception as e:
            print(e)
            print("异常")





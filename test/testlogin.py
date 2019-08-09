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

# 服务器上传
import paramiko

# 公共方法
from test import login


class login_test(login.MyTest):
    '''验证unittest自带的初始化和执行之后的方法'''
    def test_login1(self):
        '''第一次执行'''
        self.driver.find_element_by_xpath("//div[text()='账号登录']").click()
        self.driver.find_element_by_id("username_no").send_keys("13248131618")
        self.driver.find_element_by_id("password").send_keys("Test123456")
        self.driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        sleep(5)
        # sleep(1.5)
        # driver.find_element_by_xpath("//a[text()='私有']").click()
        # WebDriverWait(self.driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='艾玛同学']")))
    def test_login2(self):
        '''第二个用例'''
        self.driver.find_element_by_xpath("//div[text()='账号登录']").click()
        self.driver.find_element_by_id("username_no").send_keys('13248131618')
        self.driver.find_element_by_id("password").send_keys('Test123456')
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        WebDriverWait(self.driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='艾玛同学']")))
        sleep(0.5)
        createType = "create"
        el11 = self.driver.find_element_by_xpath("//span[text()='新建']/..")
        ActionChains(self.driver).move_to_element(el11).perform()
        sleep(3)

if __name__ == "__main__":
    unittest.main()





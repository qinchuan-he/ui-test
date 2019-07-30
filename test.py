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



# from buttonFunction.store import test_store
path = "C:\\2services\\driver\\chromedriver.exe"
url = "https://cyprex.fir.ai/sign-in"
user = "13248131618"
pwd = "Test123456"
driver = webdriver.Chrome(path)
driver.set_window_size(1400, 900)
driver.get(url)
driver.find_element_by_xpath("//div[text()='账号登录']").click()
driver.find_element_by_id("username_no").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath(
    "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
sleep(2)
driver.find_element_by_xpath("//a[text()='私有']").click()
WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='艾玛同学']")))
sleep(0.5)
el11 = driver.find_element_by_xpath("//span[text()='新建']/..")
ActionChains(driver).move_to_element(el11).perform()
driver.find_element_by_xpath("//li[text()='文件夹']").click()
sleep(0.5)
driver.switch_to.active_element.send_keys(str(time.time()))
sleep(0.5)
driver.switch_to.active_element.send_keys(Keys.ENTER)
sleep(3)








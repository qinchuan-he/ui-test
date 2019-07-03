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
# 公共方法




# 启动浏览器
def execBrower(mode):
    opt = Options()
    opt.add_argument('--disable--gpu')
    opt.add_argument('--headless')
    path = "C:\\2services\\driver\\chromedriver.exe"
    if mode==1:
        driver=webdriver.Chrome(options=opt, executable_path=path)
    else:
        driver = webdriver.Chrome(path)
    driver.set_window_size(1400, 900)  #设置窗口大小
    driver.implicitly_wait(20)
    return driver

# 登录相关
class user:
    url="https://testcyprex.fir.ai/sign-in"
    # url = "https://cyprex.fir.ai/sign-in"
    # url = "http://firai-test.gjzqth.com:4680/"
    user = "13248131618"
    # user="19956966528"
    pwd = "Test123456"
    # def __init__(self, url, user, pwd):
    #     self.url = url
    #     self.user = user
    #     self.pwd = pwd
    # 登录
    def login(self, driver):
        driver.get(self.url)
        driver.find_element_by_xpath("//div[text()='账号登录']").click()
        driver.find_element_by_id("username_no").send_keys(self.user)
        driver.find_element_by_id("password").send_keys(self.pwd)
        driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='艾玛同学']")))



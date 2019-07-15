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
    if mode == 1:
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

# 生成html相关的类
class comHtml:
    def print_html(self,picname,picpath,picid):    #就是传入名称，路径，picid就是时间
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'"+picid+"\').style.display='block';document.getElementById('fade').style.display='block'\">"+picname+"预览</a>"
            +"<div id=\""+picid+"\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'"+picid+"\').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picpath+picid+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")


#团队相关功能
class team:
    def check_team(self,driver):
        '''检查团队是否存在,不存在就创建，目前没有判断5个团队的情况的'''
        sleep(1)
        driver.find_element_by_xpath("//a[text()='团队共享']").click()
        team_name = "验证的团队"
        try:
            WebDriverWait(driver,2,0.5).until(ec.presence_of_element_located((By.XPATH,"//span[text()='验证的团队']")))
        except:
            print("团队不存在准备新建")
            driver.find_element_by_xpath("//span[text()='创建新团队并命名团队文件夹']/..").click()
            driver.find_element_by_xpath("//input[@placeholder='团队及团队文件夹名称']").send_keys(team_name)
            # driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(1)
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
            sleep(1)
        else:
            print("进入else")
        driver.find_element_by_xpath("//span[text()='验证的团队']").click()
        return team_name


# # 上传文件,,就一行代码，没必要组件化
# def com_upload(url):



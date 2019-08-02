#coding=utf-8
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#2019-06-18，增加了cookie设置，不需要每次登录
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import time   #生成时间戳用
import os    #上传autoit用
import re


# 检查搜索功能，最近收藏和数据订阅

opt = Options()
opt.add_argument("--disable-gpu") #谷歌文档提到需要加上这个属性来规避bug
opt.add_argument('--headless') #无头模式，浏览器不提供可视化页面
path="C:\\2services\\driver\\chromedriver.exe"

driver=webdriver.Chrome(path)   #有界面启动
# driver=webdriver.Chrome(options=opt,executable_path = path) #无界面启动

# 通用变量
# url="https://testcyprex.fir.ai/sign-in"
# url="https://cyprex.fir.ai/sign-in"
url="http://firai-test.gjzqth.com:4680/"

user="13248131618"
# user="19956966528"
pwd="Test123456"
picturePath="C:\\work\\1测试\\10自动化\\截图保存\\问答搜索\\"
search="股份"   
wiatTime=30
# 调整窗口大小
driver.set_window_size(1400,900)
driver.implicitly_wait(20)

driver.get(url)
driver.find_element_by_xpath("//div[text()='账号登录']").click() 
driver.find_element_by_id("username_no").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别
# driver.find_element_by_xpath("//a[text()='私有']").click()
WebDriverWait(driver,10,0.2).until(ec.presence_of_element_located((By.XPATH,"//span[text()='艾玛同学']")))


driver.find_element_by_xpath("//a[text()='智能搜索']").click()
driver.find_element_by_xpath("//div[contains(@class,'GlobalSearch_autoSearchPrefix__')]").click()
WebDriverWait(driver,5,0.2).until(ec.visibility_of_element_located((By.XPATH,"//li[text()='问答搜索']")))
driver.find_element_by_xpath("//li[text()='问答搜索']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys(search)
driver.find_element_by_xpath("//div[contains(@class,'GlobalSearch_autoSearchSuffix__')]").click()


sleep(20)
driver.get_screenshot_as_file(picturePath+"问答搜索"+str(int(time.time()))+".png")
driver.quit()




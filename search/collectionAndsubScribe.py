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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 2019-06-18，增加了cookie设置，不需要每次登录
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from common.comfunction import execBrower
from common.comfunction import user


# 检查搜索功能，最近收藏和数据订阅
# opt = Options()
# opt.add_argument('--disable--gpu')
# opt.add_argument('--headless')
# path = "C:\\2services\\driver\\chromedriver.exe"
# driver = webdriver.Chrome(path)
# driver=webdriver.Chrome(options=opt,executable_path=path) #无头模式

#mode为1是无头模式
mode=1
driver=execBrower(mode)

# 通用变量,搜索变量,保存图片路径,等待时间
search="股份"
picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\收藏订阅\\"
waitTime =  1
# # url="https://testcyprex.fir.ai/sign-in"
# url="https://cyprex.fir.ai/sign-in"
# user="13248131618"
# # user="19956966528"
# pwd="Test123456"




# 调整窗口大小
# driver.set_window_size(1400,900)
# driver.implicitly_wait(20)

user().login(driver)
# driver.get(url)
# driver.find_element_by_xpath("//div[text()='账号登录']").click()
# driver.find_element_by_id("username_no").send_keys(user)
# driver.find_element_by_id("password").send_keys(pwd)
# driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别
# WebDriverWait(driver,10,0.2).until(ec.presence_of_element_located((By.XPATH,"//span[text()='艾玛同学']")))


driver.find_element_by_xpath("//a[text()='智能搜索']").click()

sleep(waitTime)
el1=driver.find_elements_by_xpath("//section[@class='ant-layout ant-layout-has-sider']")

if len(el1) == 0:
    driver.get_screenshot_as_file(picturePath+"最近收藏截图-无内容"+str(int(time.time()))+".png")
    print("最近收藏中无内容")
else:
    WebDriverWait(driver,10,0.2).until(ec.visibility_of_element_located((By.XPATH,"//div[contains(@class,'GlobalSearchPage_tagIcon__')]")))
    driver.find_element_by_xpath("//div[contains(@class,'GlobalSearchPage_tagIcon__')]").click()
    driver.get_screenshot_as_file(picturePath+"最近收藏截图-有内容"+str(int(time.time()))+".png")
    sleep(1)
    print("最近收藏中有内容")
driver.find_element_by_xpath("//li[text()='数据订阅']").click()
sleep(waitTime)
el2=driver.find_elements_by_xpath("//div[contains(@class,'GlobalSearchPage_searchListBox__')]")
if len(el2)==0:
    driver.get_screenshot_as_file(picturePath+"数据订阅截图-无内容"+str(int(time.time()))+".png")
    print("数据订阅中无内容")
else:
    WebDriverWait(driver, 10, 0.2).until(ec.visibility_of_element_located((By.XPATH,"//div[contains(@class,'GlobalSearchPage_tagIcon__')]")))
    driver.find_element_by_xpath("//div[contains(@class,'GlobalSearchPage_tagIcon__')]").click()
    driver.get_screenshot_as_file(picturePath+"数据订阅截图-有内容"+str(int(time.time()))+".png")
    sleep(1)
    print("数据订阅中有内容")


driver.quit()





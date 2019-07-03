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
from selenium.webdriver.chrome.options import Options
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
import re

# 检查搜索功能，智能搜索，默认搜索等待3秒，超出3秒无响应会报错


opt=Options()
opt.add_argument('--disable-gpu')
opt.add_argument('--headless')
path="C:\\2services\\driver\\chromedriver.exe"
# driver=webdriver.Chrome(path)
driver=webdriver.Chrome(options=opt,executable_path=path)  #启动无头模式

# 通用变量
# url="https://testcyprex.fir.ai/sign-in"
url="https://cyprex.fir.ai/sign-in"
user="13248131618"
# user="19956966528"
pwd="Test123456"
picturePath="C:\\work\\1测试\\10自动化\\截图保存\\智能搜索\\"
search="股份"   #搜索关键字
wiatTime=15

# 调整窗口大小
driver.set_window_size(1400,900)
driver.implicitly_wait(20)

driver.get(url)
driver.find_element_by_xpath("//div[text()='账号登录']").click() 
driver.find_element_by_id("username_no").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别
WebDriverWait(driver,10,0.2).until(ec.presence_of_element_located((By.XPATH,"//span[text()='艾玛同学']")))

driver.find_element_by_xpath("//a[text()='智能搜索']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys(search)
driver.find_element_by_xpath("//div[contains(@class,'GlobalSearch_autoSearchSuffix__')]").click()

#定位标签，作为截图依据
label1="//div[contains(@class,'GlobalSearchPage_tagIcon__')]"
# WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))


# driver.find_element_by_xpath("//li[text()='公告']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字

if count==0:
    driver.get_screenshot_as_file(picturePath+"1新闻默认截图-无内容"+str(int(time.time()))+".png")
    print("新闻截图-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"1新闻默认截图-有内容"+str(int(time.time()))+".png")
    print("新闻截图-有内容")
 

# 公告
driver.find_element_by_xpath("//li[text()='公告']").click()
print(count)
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
print(count)
if count==0:
    driver.get_screenshot_as_file(picturePath+"2公告-沪深默认截图-无内容"+str(int(time.time()))+".png")
    print("完成公告-沪深无内容截图-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"2公告-沪深默认截图-有内容"+str(int(time.time()))+".png")
    print("完成公告-沪深有内容截图-有内容")


driver.find_element_by_xpath("//li[text()='预披露']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"3公告-预披露截图-无内容"+str(int(time.time()))+".png")
    print("完成公告-预披露截图-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"3公告-预披露截图-有内容"+str(int(time.time()))+".png")
    print("完成公告-预披露截图-有内容")

driver.find_element_by_xpath("//li[text()='反馈审核']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"4公告-反馈审核截图-无内容"+str(int(time.time()))+".png")
    print("完成公告-反馈审核截图-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"4公告-反馈审核截图-有内容"+str(int(time.time()))+".png")
    print("完成公告-反馈审核截图-有内容")

driver.find_element_by_xpath("//li[text()='科创']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"5公告-科创截图-无内容"+str(int(time.time()))+".png")
    print("完成公告-科创截图-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"5公告-科创截图-有内容"+str(int(time.time()))+".png")
    print("完成公告-科创截图-有内容")

driver.find_element_by_xpath("//li[text()='证监监管']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"6公告-证监监管-无内容"+str(int(time.time()))+".png")
    print("完成公告-证监监管-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"6公告-证监监管-有内容"+str(int(time.time()))+".png")
    print("完成公告-证监监管-有内容")

driver.find_element_by_xpath("//li[text()='沪深']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"7公告-沪深-无内容"+str(int(time.time()))+".png")
    print("完成公告-沪深-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"7公告-沪深-有内容"+str(int(time.time()))+".png")
    print("完成公告-沪深-有内容")

#智库
driver.find_element_by_xpath("//li[text()='智库']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"8智库-研报默认-无内容"+str(int(time.time()))+".png")
    print("完成智库-智库默认-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"8智库-研报默认-有内容"+str(int(time.time()))+".png")
    print("完成智库-智库默认-有内容")

driver.find_element_by_xpath("//li[text()='自媒体']").click()
sleep(5)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"9智库-自媒体-无内容"+str(int(time.time()))+".png")
    print("完成智库-自媒体-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"9智库-自媒体-有内容"+str(int(time.time()))+".png")
    print("完成智库-自媒体-有内容")

driver.find_element_by_xpath("//li[contains(@class,'CustomizeClassifiedNav_tabNavItem__') and contains(text(),'智库')]").click()   #可以定位到
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"10智库-智库-无内容"+str(int(time.time()))+".png")
    print("完成智库-智库-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"10智库-智库-有内容"+str(int(time.time()))+".png")
    print("完成智库-智库-有内容")

driver.find_element_by_xpath("//li[text()='研报']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"11智库-研报-无内容"+str(int(time.time()))+".png")
    print("完成智库-研报-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"11智库-研报-有内容"+str(int(time.time()))+".png")
    print("完成智库-研报-有内容")

# 点击新闻验证可点击
driver.find_element_by_xpath("//li[text()='新闻']").click()
sleep(wiatTime)
result=driver.find_element_by_xpath("//div[@class='ant-col ant-col-17']").text    #获取搜索结果
count=int(re.findall("[0-9]+",result)[0]) #获取其中的数字
if count==0:
    driver.get_screenshot_as_file(picturePath+"12新闻-无内容"+str(int(time.time()))+".png")
    print("完成新闻-无内容")
else:
    WebDriverWait(driver,15,0.2).until(ec.presence_of_element_located((By.XPATH,label1)))
    driver.get_screenshot_as_file(picturePath+"12新闻-有内容"+str(int(time.time()))+".png")
    print("完成新闻-有内容")

print("全部执行完成")

driver.quit()
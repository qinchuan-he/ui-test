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
# driver=webdriver.Chrome(path)   #有界面启动

driver=webdriver.Chrome(options=opt,executable_path = path) #无头模式
# driver.maximize_window()
driver.set_window_size(1400,900)  # 调整窗口大小

# 通用变量,搜索变量,保存图片路径,等待时间
# search="公司"
search="股份"
picturePath="C:\\work\\1测试\\10自动化\\截图保存\\边写边搜\\"
waitTime=12
url="https://testcyprex.fir.ai/sign-in"
# url="https://cyprex.fir.ai/sign-in"
# url = "http://firai-test.gjzqth.com:4680/sign-in"
# user="19956966528"
user="13248131618"
pwd="Test123456"




driver.implicitly_wait(20)

driver.get(url)
driver.find_element_by_xpath("//div[text()='账号登录']").click() 
driver.find_element_by_id("username_no").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别
WebDriverWait(driver,10,0.2).until(ec.presence_of_element_located((By.XPATH,"//span[text()='艾玛同学']")))

# 新建文档
el1=driver.find_element_by_xpath("//span[text()='新建']")
ActionChains(driver).move_to_element(el1).perform()
driver.find_element_by_xpath("//li[text()='新建文档']").click()
WebDriverWait(driver,10,0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))

driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()

WebDriverWait(driver,5,0.2).until(ec.presence_of_element_located((By.XPATH,"//div[text()='私有与共享']")))
driver.find_element_by_xpath("//input[contains(@placeholder,'搜')]").send_keys(search)
driver.switch_to.active_element.send_keys(Keys.ENTER)

sleep(waitTime)
driver.get_screenshot_as_file(picturePath+"默认列表截图"+str(int(time.time()))+".png")

strcountlist=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchToolbar__')]/span[1]")
# print(strcountlist[0].text)
count=int(re.findall("[0-9]+",strcountlist[0].text)[0])
print("私有共享资源数量： %d" %count)
if count>0:
    el2=driver.find_element_by_xpath("//div[@class='ant-spin-container']/div[1]")
    ActionChains(driver).move_to_element(el2).perform()
    # el2.click()
    # sleep(waitTime)
    # driver.get_screenshot_as_file(picturePath+"默认列表展开截图"+str(int(time.time()))+".png")
    # ActionChains(driver).move_to_element(el2).perform()
    el21=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchContentItem__')]")  #el2开头的都是打开列表的
    if len(el21)!=0:
        el31= el21[0].text
        if len(el31)!=0:
            el21[0].click()
        sleep(1)
        driver.get_screenshot_as_file(picturePath+"默认列表展开截图"+str(int(time.time()))+".png")
    ActionChains(driver).move_to_element(el2).perform()
    el11=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]//i[@class='anticon anticon-arrows-alt']")
    ActionChains(driver).move_to_element(el11[0]).perform()
    el11[0].click()
    sleep(waitTime)
    driver.get_screenshot_as_file(picturePath+"默认双屏"+str(int(time.time()))+".png")
    driver.find_element_by_xpath("//i[@class='anticon anticon-shrink']").click()

# 中场切换
driver.find_element_by_xpath("//span[text()='关闭搜索']/..").click()
driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()
sleep(1)
driver.find_element_by_xpath("//input[contains(@placeholder,'搜')]").send_keys(search)
driver.switch_to.active_element.send_keys(Keys.ENTER)
sleep(waitTime)
# 查询公告
driver.find_element_by_xpath("//div[text()='公告']").click()
sleep(waitTime)
driver.get_screenshot_as_file(picturePath+"公告列表截图"+str(int(time.time()))+".png")

strcountlist2=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchToolbar__')]/span[1]")
count2=int(re.findall("[0-9]+",strcountlist2[1].text)[0])
print("公告数量： %d" %count2)
show=1
if count>20:
    show=21
else:
    show=count+1
# print("show: %d" %show)
if count2>0:
    # el3=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchTitle__')]")
    el3=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]")
    ActionChains(driver).move_to_element(el3[1]).perform()
    el22=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchBody__')]")
    print(len(el22))
    if len(el22)!=0:
        el32=el22[0].text
        if len(el32)!=0:
            el22[0].click()
        sleep(1)
        driver.get_screenshot_as_file(picturePath+"公告列表展开截图"+str(int(time.time()))+".png")
    ActionChains(driver).move_to_element(el3[1]).perform()
    el4=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]//i[@class='anticon anticon-arrows-alt']")
    # print("el4的长度： %d" %len(el4))
    ActionChains(driver).move_to_element(el4[1]).perform()
    el4[1].click()
    sleep(waitTime)
    driver.get_screenshot_as_file(picturePath+"公告双屏"+str(int(time.time()))+".png")
    driver.find_element_by_xpath("//i[@class='anticon anticon-shrink']").click()


# 中场切换
driver.find_element_by_xpath("//span[text()='关闭搜索']/..").click()
driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()
sleep(1)
driver.find_element_by_xpath("//input[contains(@placeholder,'搜')]").send_keys(search)
driver.switch_to.active_element.send_keys(Keys.ENTER)
sleep(waitTime)

# 查询研报
driver.find_element_by_xpath("//div[text()='研报']").click()
sleep(waitTime)
driver.get_screenshot_as_file(picturePath+"研报列表截图"+str(int(time.time()))+".png")

strcountlist3=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchToolbar__')]/span[1]")
count3=int(re.findall("[0-9]+",strcountlist3[1].text)[0])
print("研报查询结果数： %d" %count3)
show=1
if count2>20:
    show=21
else:
    show=count2+1
if count3>0:
    el5=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]")
    ActionChains(driver).move_to_element(el5[1]).perform()
    # el5[1].click()
    # sleep(waitTime)
    # driver.get_screenshot_as_file(picturePath+"研报列表展开截图"+str(int(time.time()))+".png")
    # ActionChains(driver).move_to_element(el5[1]).perform()
    el23=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchBody__')]")  
    print(len(el23))
    if len(el23)>=show-1:
        el33= el23[show-1].text
        if len(el33)!=0:
            el23[show-1].click()
        sleep(1)
        driver.get_screenshot_as_file(picturePath+"研报列表展开截图"+str(int(time.time()))+".png")
    ActionChains(driver).move_to_element(el5[1]).perform()
    el6=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]//i[@class='anticon anticon-arrows-alt']")
    ActionChains(driver).move_to_element(el6[1]).perform()
    el6[1].click()
    sleep(waitTime)
    driver.get_screenshot_as_file(picturePath+"研报双屏截图"+str(int(time.time()))+".png")
    driver.find_element_by_xpath("//i[@class='anticon anticon-shrink']").click()

# 中场切换
driver.find_element_by_xpath("//span[text()='关闭搜索']/..").click()
driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()
sleep(1)
driver.find_element_by_xpath("//input[contains(@placeholder,'搜')]").send_keys(search)
driver.switch_to.active_element.send_keys(Keys.ENTER)
sleep(waitTime)

# 查询智库
driver.find_element_by_xpath("//div[text()='智库']").click()
sleep(waitTime)
driver.get_screenshot_as_file(picturePath+"智库列表截图"+str(int(time.time()))+".png")
strcountlist4=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchToolbar__')]/span[1]")
count4=int(re.findall("[0-9]+",strcountlist4[1].text)[0])
print("智库查询结果数： %d" %count3)
show=1
if count3>20:
    show=21
else:
    show=count3+1
if count4>0:
    el7=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]")
    ActionChains(driver).move_to_element(el7[1]).perform()
    # el7[1].click()
    # sleep(waitTime)
    # driver.get_screenshot_as_file(picturePath+"智库列表展开截图"+str(int(time.time()))+".png")
    # ActionChains(driver).move_to_element(el7[1]).perform()
    el24=driver.find_elements_by_xpath("//div[contains(@class,'SearchFileContentPanel_searchBody__')]")
    print(len(el24))
    if len(el24)>=show:
        el34=el24[show-1].text
        if len(el34)!=0:
            el24[show-1].click()
        sleep(1)
        driver.get_screenshot_as_file(picturePath+"智库列表展开截图"+str(int(time.time()))+".png")
    ActionChains(driver).move_to_element(el7[1]).perform()
    el8=driver.find_elements_by_xpath("//div[@class='ant-spin-container']/div[1]//i[@class='anticon anticon-arrows-alt']")
    ActionChains(driver).move_to_element(el8[1]).perform()
    el8[1].click()
    sleep(waitTime)
    driver.get_screenshot_as_file(picturePath+"智库双屏截图"+str(int(time.time()))+".png")

driver.find_element_by_xpath("//span[text()='关闭搜索']/..").click()
sleep(waitTime)
driver.quit()


